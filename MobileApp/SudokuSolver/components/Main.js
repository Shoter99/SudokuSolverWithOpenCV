import { Button, FlatList, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import React from "react";
import Grid from "./Grid";

const Main = () => {
  const grid = [
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
  ];
  return (
    <View style={styles.container}>
      {grid.map((elem, index) => {
        return <Grid key={index} grid={elem} />;
      })}
      {/* <TouchableOpacity style={styles.solveBtn}>
          <Text style={styles.text}>
              Solve
          </Text>
      </TouchableOpacity> */}
    </View>
  );
};

export default Main;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "row",
    flexWrap: "wrap",
    marginTop: "5%",
    padding: 0,
    width: "100%",
    alignItems: "center",
    justifyContent: "center"
  },
  text: {
    fontSize: 20,
  },
    solveBtn: {
        backgroundColor: '#cdcdcd',
        borderRadius: 5,
        paddingHorizontal: 15,
        paddingVertical: 5,
        margin: 10,
    }

});
