import requests
from geopy.geocoders import Nominatim
import argparse
from transformers import BertModel, BertTokenizer
import transformers
import scipy.spatial.distance as ds
from datetime import datetime

transformers.logging.set_verbosity_error()

transaction_class_list = ['Продукты', 'Еда', 'Инструменты', 'Одежда', 'Техника', 'автозапчасти']

#parser = argparse.ArgumentParser(description='')
#parser.add_argument('input', metavar='N', type=str, nargs='+',
#                    help='a string')
#args = parser.parse_args()

print('Что Вы хотите открыть?')
input = input()

sbert = BertModel.from_pretrained('sberbank-ai/ruBert-base', output_attentions=False, output_hidden_states=False)
sbert.eval()
sbert_tokenizer = BertTokenizer.from_pretrained('sberbank-ai/ruBert-base')

def _sbert_get_vector(input_ids):
    embeddings = sbert(input_ids)
    return embeddings['last_hidden_state'].reshape([1, -1]).detach().numpy()

def _sbert_tokenize_sentence(text):
    encoded_dict = sbert_tokenizer.encode_plus(
                        text,                      # Sentence to encode.
                        add_special_tokens = False, # Add '[CLS]' and '[SEP]'
                        max_length = 16,           # Pad & truncate all sentences.
                        return_tensors = 'pt',
                        padding = 'max_length',
                        truncation=True
                   )
    return encoded_dict['input_ids'].reshape([1, -1])

#all_users = requests.get('http://188.225.57.152:8005/api/user/all/')
#all_users = all_users.json()

all_tags = requests.get('http://188.225.57.152:8005/api/hash/all')
all_tags = all_tags.json()

all_transactions = requests.get('http://188.225.57.152:8005/api/transaction/all')
all_transactions = all_transactions.json()

tags_text = list(map(lambda t: (t['id'], t['text']), all_tags))
tags_tokenized = list(map(lambda t: _sbert_tokenize_sentence(t[1]), tags_text))
tags_embedings = list(map(lambda t: _sbert_get_vector(t), tags_tokenized))
input_embeddings = _sbert_get_vector(_sbert_tokenize_sentence(input))
distances = [ds.cosine(action_embeddings, input_embeddings) for action_embeddings in tags_embedings]
distances = [(tags_text[i][0], distances[i]) for i in range(len(distances))]
distances = list(sorted(distances, key=lambda d: d[1]))
best_id = distances[0][0]


transactions_tokenized = list(map(lambda t: (t['place'], _sbert_tokenize_sentence(t['place'])), all_transactions))
transaction_embeddings = list(map(lambda t: _sbert_get_vector(t[1]), transactions_tokenized))

distances_transaction = [ds.cosine(action_embeddings, input_embeddings) for action_embeddings in transaction_embeddings]
distances_transaction = [(transactions_tokenized[i][0], distances_transaction[i]) for i in range(len(distances_transaction))]
distances_transaction = list(sorted(distances_transaction, key=lambda d: d[1]))
best_transaction_text = distances_transaction[0][0]

all_transactions = list(filter(lambda t: t['place'] == best_transaction_text, all_transactions))

best_tag_text = None
for id, text in tags_text:
    if id == best_id:
        best_tag_text = text
        break

all_likes = requests.get('http://188.225.57.152:8005/api/like/list?hash_id=' + str(best_id))
all_likes = all_likes.json()

times = []
for like in all_likes.values():
    times.append(datetime.strptime(like['date'][:-5], '%Y-%m-%dT%H:%M:%S').hour)
middle_ad_time = int(sum(times) / len(times))

times = []
for transaction in all_transactions:
    times.append(datetime.strptime(transaction['date'][:-8], '%Y-%m-%dT%H:%M:%S').hour)
middle_work_time = int(sum(times) / len(times))

news_ids = set(map(lambda l: l['post_id'], all_likes.values()))
news = []
for id in news_ids:
    news.append(requests.get('http://188.225.57.152:8005/api/post-hash/detail?post_id=' + str(id)).json())

interests = []
for new in news:
    interests.extend(new['hashtags'])
interests = list(set(interests))

user_ids = set(map(lambda l: l['user_id'], all_likes.values()))
all_users = []
for id in news_ids:
    all_users.append(requests.get('http://188.225.57.152:8005/api/user/detail/' + str(id)).json())

middle_age = 0
for user in all_users:
    middle_age += user['age']
middle_age /= len(all_users)
middle_age = int(middle_age)

all_realty = requests.get('http://188.225.57.152:8005/api/realty/all')
all_realty = all_realty.json()

longitude = 0
lattitude = 0
counter = 0
for user in all_users:
    if user['longitude']:
        longitude += user['longitude']
        lattitude += user['latitude']
        counter += 1
if counter != 0:
    longitude /= counter
    lattitude /= counter

realty_distances = []
for realty in all_realty:
    lon, lat = realty['longitude'], realty['latitude']
    lon, lat = lon - longitude, lat - lattitude
    dist = lon * lon + lat * lat
    realty_distances.append((dist, realty))
realty_distances = list(sorted(realty_distances))
nearest_realty = realty_distances[0][1]

geolocator = Nominatim(user_agent="my_request")
location = geolocator.reverse(f"{lattitude}, {longitude}")

print('Средний возраст ЦА:', middle_age)
print('Лучшее время для рекламных статей:', middle_ad_time)
print('Наибольшая покупательская активность:', middle_work_time)
print('Категория транзакций:', best_transaction_text)
print('Дополнительные интересы аудитории:', ', '.join(interests))
print('Самая проходная точка:', location.address)
print('Ближайшая арендуемая недвижимость:', nearest_realty['place'])