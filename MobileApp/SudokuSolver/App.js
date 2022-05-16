import React, { useState } from "react";
import {
  View,
  StyleSheet,
  Image,
  Text,
  TouchableOpacity,
  StatusBar,
  Alert,
} from "react-native";
import * as ImagePicker from "expo-image-picker";
import AppBar from "./components/AppBar";
import Main from "./components/Main";
import ExpoStatusBar from "expo-status-bar/build/ExpoStatusBar";

export default function ImagePickerExample() {
  const URI = "https://0746-85-237-187-72.eu.ngrok.io";
  // const URI = "https://0746-85-237-187-7.eu.ngrok.io"
  const [waitingForResponse, setWaitingForResponse] = useState(false);
  const [grid, setGrid] = useState([
    [" ", "2", " ", "4", " ", "6", " ", " ", " "],
    [" ", " ", " ", " ", " ", "5", " ", "7", " "],
    [" ", " ", " ", "1", " ", " ", " ", "3", " "],
    [" ", "1", " ", "8", " ", "2", " ", "9", " "],
    [" ", " ", "2", " ", "5", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", "7", "8", " ", " "],
    [" ", " ", " ", "5", " ", "8", "9", " ", " "],
    ["4", " ", " ", " ", " ", "6", " ", " ", " "],
    [" ", " ", "1", "4", " ", " ", " ", " ", " "],
  ]);

  const sendErrorAlert = (message) => {
    Alert.alert(
      "Error",
      message,
      [{ text: "OK", onPress: () => console.log("OK Pressed") }],
      { cancelable: false }
    );
  };

  const sendSuccessAlert = (message) => {
    Alert.alert(
      "Success",
      message,
      [{ text: "OK", onPress: () => console.log("OK Pressed") }],
      { cancelable: false }
    );
  };

  const fetchSolution = async () => {
    setWaitingForResponse(true);
    // console.log(JSON.stringify({board:grid}))
    fetch(`${URI}/api/solve`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        board: grid,
      }),
    })
      .then((res) => {
        if (res.status === 200) {
          data = res
            .json()
            .then((data) => {
              if (data === "Cannot solve")
                sendErrorAlert("Cannot solve this sudoku, try different one.");
              else {
                console.log(data);
                setGrid(data);
              }
            })
            .catch((err) =>
              sendErrorAlert("Something Wrong! Try again later.")
            );
        } else {
          throw new Error(res.statusText);
        }
      })
      .catch((err) => {
        sendErrorAlert("Server not responding! Try again later.");
      })
      .finally(() => {
        setWaitingForResponse(false);
      });
    // console.log(data)
  };

  const createFormData = (photo) => {
    const data = new FormData();
    console.log(photo.uri);
    data.append("photo", {
      name: "board",
      type: "image/jpeg",
      uri: Platform.OS === "ios" ? photo.uri.replace("file://", "") : photo.uri,
    });
    return data;
  };

  const [image, setImage] = useState(null);

  const pickImage = async () => {
    // No permissions request is necessary for launching the image library
    let result = await ImagePicker.launchCameraAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      quality: 1,
    });

    // console.log(result);

    if (!result.cancelled) {
      const formData = createFormData(result);
      // console.log(formData);
      fetch(`${URI}/api/read_numbers`, {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        body: formData,
      })
        .then((response) => response.json())
        .then((res) => {
          sendSuccessAlert(res);
        })
        .catch((err) => sendErrorAlert("Server not responding!"));
    }
  };

  return (
    <View style={styles.screen}>
      <AppBar></AppBar>
      {waitingForResponse ? (
        <View style={{ flex: 1, justifyContent: "center" }}>
          <Image
            style={{ width: 150, height: 150 }}
            source={require("./assets/loading.gif")}
          ></Image>
        </View>
      ) : (
        <Main grid={grid} fetchSolution={fetchSolution}></Main>
      )}
      {image && (
        <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />
      )}

      <TouchableOpacity style={styles.cameraBtn} onPress={pickImage}>
        <Text style={{ fontSize: 29 }}>📷</Text>
      </TouchableOpacity>
      <ExpoStatusBar></ExpoStatusBar>
    </View>
  );
}

const styles = StyleSheet.create({
  cameraBtn: {
    backgroundColor: "#ccc",
    borderRadius: 50,
    padding: 20,
    marginBottom: 40,
  },
  screen: {
    marginTop: StatusBar.currentHeight,
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#333",
  },
  container: {
    flex: 1,
  },
  loading: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    color: "white",
  },
});
