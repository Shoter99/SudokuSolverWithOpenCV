import React, { useState } from "react";
import {
  View,
  StyleSheet,
  Image,
  StatusBar,
  Alert,
} from "react-native";
import * as ImagePicker from "expo-image-picker";
import AppBar from "./components/AppBar";
import Main from "./components/Main";


export default function ImagePickerExample() {
  const URI = "https://0746-85-237-187-72.eu.ngrok.io";
  // const URI = "https://0746-85-237-187-7.eu.ngrok.io"
  const DEFAULT_GRID = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
  ]
  const [grid, setGrid] = useState(DEFAULT_GRID)

  const clearGrid = () =>
  {
    setGrid(DEFAULT_GRID)
  }

  const changeValue = (idx, idy, val) => {
    // console.log(idx, idy, val);
    let newGrid = [...grid]
    // console.log(newGrid);
    newGrid[idx][idy] = val == "" ? " " : val
    setGrid(newGrid)
  }

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
          res
            .json()
            .then((data) => {
              if (data === "Cannot solve")
                sendErrorAlert("Cannot solve this sudoku, try different one.");
              else {
                // console.log(data);
                setGrid(data);
              }
            })
            .catch((err) =>
              sendErrorAlert("Something Wrong! Try again later."+err.message)
            );
        } else {
          throw new Error(res.statusText);
        }
      })
      .catch((err) => {
        sendErrorAlert("Server not responding! Try again later."+err.message);
      })
      .finally(() => {
        setWaitingForResponse(false);
      });
    // console.log(data)
  };

  const createFormData = (photo) => {
    const data = new FormData();
    // console.log(photo.uri);
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
        <Main changeValue={changeValue} clearGrid={clearGrid} grid={grid} pickImage={pickImage} fetchSolution={fetchSolution}></Main>
        )}   
    </View>
  );
}

const styles = StyleSheet.create({
  cameraBtn: {
    backgroundColor: "#00ADB5",
    borderRadius: 50,
    padding: 20,
    position: "absolute",
    bottom: "5%",

  },
  screen: {
    marginTop: StatusBar.currentHeight,
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#393E46",
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
