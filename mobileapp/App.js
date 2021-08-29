
import React, { useEffect, useState } from 'react';
import { Text, View, Alert, Item, ScrollView, TextInput, StyleSheet, SafeAreaView, Button, CheckBox, Image } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';
import Icon from "react-native-vector-icons/Ionicons";
import * as axios from 'axios';

function HomeScreen() {
 
  
  const [appState, setAppState] = useState();
  const [appLike, setAppLike] = useState();
  const [Like, setLike] = useState();
  const [userID, serUserID] = useState(7);

  const apiUrl = 'http://188.225.57.152:8005/api';

  
  
  useEffect(() => {
    //const apiUrl = 'http://188.225.57.152:8005/api/post/all/';
    axios.get(apiUrl+'/post/all/').then((resp) => {
      const allPersons = resp.data;
      setAppState(allPersons);
      //console.log(appState) justifyContent: 'center'
    });

    //const apiUrl = 'http://188.225.57.152:8005/api/like/all/';
     axios.get(apiUrl+'/like/all/').then((response) => {
      const allLike = response.data;
      setAppLike(allLike);
      //console.log(response.status) // justifyContent: 'center'
      //response.status=='200' ? resolve() : null
    });

  }, [setAppState]);

  let likes;
  console.log(appState)
  console.log(appLike) 
  let promise = new Promise((resolve, reject) => {
  appLike ? resolve() : null
});
  //countLike();
  

  promise
  .then(
    result => {
      // первая функция-обработчик - запустится при вызове resolve
      //countLike() // result - аргумент resolve
      // error - аргумент reject
      countLike();
    },
    error => {
      // вторая функция - запустится при вызове reject
      alert("Rejected: "); // error - аргумент reject
    }
  );

  
  
  let countLike = () => {
     likes = new Array(appLike.length).fill(0);
    
    for (let i = 0; i < appLike.length; i++) { // выведет 0, затем 1, затем 2
      //console.log(appLike[i])
      //console.log(appState[appLike[i].post].id)
      //console.log(appState[i])
      //console.log(appLike[i].post)
      //likes[appLike[i].post]==NaN ? likes[appLike[i].post]=0 : null
      likes[appLike[i].post]=likes[appLike[i].post]+1;
      //setLike(Like[appLike[i].post]++);
      //console.log(appState[appLike[i].post]);
      // appState[appLike[i].post]!=NaN ? setAppState(appState[appLike[i].post].like++) : null
    }
    console.log(likes);
    //setLike(likes)
  }

  let getLike = (id) => {
    var positiveArr = appLike.filter(function(number) {
      return number.post == id;
    });
    
    return positiveArr.length
  }  

  let imgLike = (id) => {
    
    let arrsome = appLike.some((item)=>item.user==userID &&  item.post==id)
    
    //console.log("aa ",arrsome)
    return arrsome
  }

  const addlike = (id) => {
    //console.log(id);
    axios.post(apiUrl+'/like/create/', {"user": userID,"post": id}).then((resp) => {
      const allPersons = resp.data;
      //setAppState(allPersons);
      //console.log(appState) justifyContent: 'center'
    });

    axios.get(apiUrl+'/like/all/').then((response) => {
      const allLike = response.data;
      setAppLike(allLike);
      //console.log(response.status) // justifyContent: 'center'
      //response.status=='200' ? resolve() : null
    });

  }
 
  return (
    <View style={{ flex: 1 }}>
      <View style={{ backgroundColor: '#0d6ab0', alignItems: 'center', justifyContent: 'center', width: "100%", height: 80}}>
        <Text style={{ paddingTop: '5%', color: 'white', fontSize: 20}}>Новости</Text>
      </View>
       
      <ScrollView showsVerticalScrollIndicator={false}>
      {appState ? appState.map((i) => 
      
      <View value={i.key} style={{ backgroundColor: 'white', borderRadius: 10,  shadowOpacity: 0.3, shadowRadius: 6.27, marginLeft: '4%', marginTop: '2%', paddingTop: '2%', paddingLeft: '2%', paddingBottom: '%', width: "90%", flex: "auto" }} 
      key={i.id }>
      <View>
      <Text style={{fontWeight: "bold", paddingBottom: "2%", fontSize: 15}}>{i.title}</Text> 
      </View>
      <Text>{i.text}</Text>
      <View >
      <View>  
      <View style={{  position: "relative", top: 4, alignSelf: 'flex-end', paddingRight: "2%", paddingBottom: "2%"}}> 
      
      {appLike && imgLike(i.id) ?
    <Icon.Button
    key={i.id }
    name="heart-sharp" 
    backgroundColor="#0d6ab0"
    onPress={()=>addlike(i.id)}
    > 
  {appLike ? <Text style={{  color: 'white'}}>{getLike(i.id)}</Text>
  : null}
  </Icon.Button>
  :
  <Icon.Button
  key={i.id }
  name="heart-outline" 
  backgroundColor="#0d6ab0"
  onPress={()=>addlike(i.id)}
>{appLike ? <Text style={{  color: 'white'}}>{getLike(i.id)}</Text>
: null}
</Icon.Button>
      }
  </View>
     
  </View>
      </View>
      </View>) 
      : <Text>'loading...'</Text>}
   </ScrollView>
    </View>
    
  );

}

function Auth() {

  const [Name, onChangeName] = React.useState(null);
  const [City, onChangeCity] = React.useState(null);
  const [Old, onChangeOld] = React.useState(null);
  const [Sex, onChangeSex] = React.useState(true);
  
  return (
    <SafeAreaView>
      <TextInput
        style={styles.input}
        onChangeText={onChangeName}
        value={Name}
        placeholder="Имя"
      />
      <TextInput
        style={styles.input}
        onChangeText={onChangeCity}
        value={City}
        placeholder="Город"
        keyboardType="Surename"
      />
        <TextInput
        style={styles.input}
        onChangeText={onChangeOld}
        value={Old}
        placeholder="Возраст"
        keyboardType="Surename"
      />
      
      <View style={{backgroundColor: "#0d6ab0"}}><Button
  //onPress={onPressLearnMore}
  title="Войти"
  color="#fff"
  accessibilityLabel="Войти"
/></View>
      
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
});

function Transaction() {
  
  const [transaction, setTransaction] = useState(null);

  const apiUrl = 'http://188.225.57.152:8005/api';
  
  useEffect(() => {
    //const apiUrl = 'http://188.225.57.152:8005/api/post/all/';
    axios.get(apiUrl+'/transaction/all/').then((resp) => {
      const allTransaction = resp.data;
      
      setTransaction(allTransaction);
      console.log(resp.data) 
    });

  }, [setTransaction]);

  console.log(transaction)

  let DateFormat = (str) => {
    var date = new Date(str);
    return date.toLocaleString('ru', options)
  }
  
  var options = {
    day: 'numeric',
    month: 'numeric',
    year: 'numeric'
  }
    

  return (
    <View style={{ flex: 1 }}>
      <View style={{ backgroundColor: '#0d6ab0', alignItems: 'center', justifyContent: 'center', width: "100%", height: 80}}>
        <Text style={{ paddingTop: '5%', color: 'white', fontSize: 20}}>Транзакции</Text>
      </View>
       
      <ScrollView showsVerticalScrollIndicator={false}>
      {transaction ? transaction.map((i) => 
      <View value={i.key} style={{ backgroundColor: 'white', borderRadius: 10,  shadowOpacity: 0.3, shadowRadius: 6.27, marginLeft: '4%', marginTop: '2%', paddingTop: '1%', paddingLeft: '2%', paddingBottom: '2%', width: "90%", height: 100 }} 
      key={i.id }>
      <View style={{ flexDirection: 'row'}}>
      <Text style={{fontSize: 20}}>{i.place+"  "}</Text>
      </View>
      <Text style={{fontSize: 20, flexDirection: 'row', alignSelf: 'flex-end', paddingRight: "2%", paddingEnd: "3%"}}>{i.sum+" ₽"}</Text>
      <Text>{DateFormat(i.date)}</Text>
      </View>
      )
      : <Text>'loading...'</Text>
    }
   </ScrollView>
    </View>
  
  );
}

function UserProfile() {
  const [userID, setUserID] = useState(7);
  const [userProfile, setUserProfile] = useState(null);

  const apiUrl = 'http://188.225.57.152:8005/api';
  
  useEffect(() => {
    //const apiUrl = 'http://188.225.57.152:8005/api/post/all/';
    axios.get(apiUrl+'/user/detail/'+userID).then((resp) => {
      const allProfile = resp.data;
      
      setUserProfile(allProfile);
      console.log(resp) 
    });

  }, [setUserProfile]);


    

  return (
    <View style={{ flex: 1 }}>
      <View style={{ backgroundColor: '#0d6ab0', alignItems: 'center', justifyContent: 'center', width: "100%", height: 80}}>
        <Text style={{ paddingTop: '5%', color: 'white', fontSize: 20}}>Профиль</Text>
      </View>
       
      <ScrollView showsVerticalScrollIndicator={false}>
     <View style={{ alignItems: 'center', justifyContent: 'center'}}>
       <View>
        <Text>{""}</Text> 
       </View>
       
       <Image
        style={{width: 150, height: 150, borderRadius: "100%", marginTop: "5%"}}
        source={{
          uri: 'https://cdn.pixabay.com/photo/2014/04/03/10/32/businessman-310819_1280.png',
        }}
      />
      
       <View>
        {userProfile ? <Text style={{ paddingTop: '5%', fontSize: 20}}>{userProfile.name}</Text> : <Text>load</Text>}
       </View>
       <View>
        {userProfile ? <Text style={{ paddingTop: '5%', fontSize: 15}}>{userProfile.gender ? 'Мужчина' : "Женищна"}</Text> : <Text>load</Text>}
       </View>
       <View>
        {userProfile ? <Text style={{ paddingTop: '5%', fontSize: 15}}>{userProfile.address}</Text> : <Text>load</Text>}
       </View>
     </View>
   </ScrollView>
    </View>
  
  );
}

const Tab = createMaterialBottomTabNavigator();

export default function App() {

  const [isAuth, serAuth] = useState(true);

  return (
    isAuth ? 
    <NavigationContainer>
      <Tab.Navigator
        initialRouteName="Home"
        activeColor="#f0edf6"
        inactiveColor="#3e2465"
        barStyle={{ backgroundColor: '#0d6ab0' }}
      >
        <Tab.Screen name="Новости" component={HomeScreen} />
        <Tab.Screen name="Транзакции" component={Transaction} />
        <Tab.Screen name="Профиль" component={UserProfile} />
      </Tab.Navigator>
    </NavigationContainer>
    :
    <Auth/>
  );
}


