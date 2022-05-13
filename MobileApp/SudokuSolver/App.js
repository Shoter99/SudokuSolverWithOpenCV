import React, { useState } from 'react';
import { View,  StyleSheet, Image, Text, TouchableOpacity, StatusBar } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import AppBar from './components/AppBar';
import Main from './components/Main';

export default function ImagePickerExample() {
  const [image, setImage] = useState(null);

  const pickImage = async () => {
    // No permissions request is necessary for launching the image library
    let result = await ImagePicker.launchCameraAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      quality: 1,
    });

    console.log(result);

    if (!result.cancelled) {
      setImage(result.uri);
    }
  };

  return (
    <View style={styles.screen}>
      <AppBar></AppBar>
      <Main ></Main>
      {image && <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}
      <TouchableOpacity style={styles.cameraBtn} onPress={pickImage}>
        <Text style={{fontSize:29}}>
            📷
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  cameraBtn: {
    backgroundColor: '#ccc',
    borderRadius: 50,
    padding: 20,
    marginBottom: 20,
},
  screen: {
    marginTop: StatusBar.currentHeight,
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#333',

  },
 container: {
  flex: 1 
 },
})