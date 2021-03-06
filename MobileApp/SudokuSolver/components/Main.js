import { Button, FlatList, ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import {React, useState} from "react";
import Grid from "./Grid";
import {Icon } from 'react-native-elements'


const Main = ({grid, fetchSolution, pickImage, changeValue, clearGrid}) => {
  
  return (
    <View style={styles.container}>
      {grid.map((elem, index) => {
        return <Grid changeValue={changeValue} key={index} idx={index} grid={elem} />;
      })}
      <ScrollView >
      <View style={{ 
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center', 
        alignItems: 'center',
      }}>

      <TouchableOpacity onPress={fetchSolution} style={styles.solveBtn}>
          <Text style={styles.text}>
              Solve
          </Text>  
      </TouchableOpacity>


      <TouchableOpacity onPress={clearGrid} style={styles.solveBtn}>
          <Text style={styles.text}>
              Clear
          </Text>
      </TouchableOpacity>
      </View>
      <View style={{    alignItems: "center",
    justifyContent: "center"}}>

      <TouchableOpacity style={styles.cameraBtn} onPress={pickImage}>
        <Icon name="camera" type="font-awesome" color="#222831" />
      </TouchableOpacity>
      </View>
      </ScrollView>
    </View>
  );
};

export default Main;

const styles = StyleSheet.create({
  cameraBtn: {
    backgroundColor: "#00ADB5",
    borderRadius: 50,
    padding: 20,
    width: 200,


  },
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
    color: '#222831'
  },
    solveBtn: {
        backgroundColor: '#00ADB5',
        borderRadius: 5,
        paddingHorizontal: 15,
        paddingVertical: 5,
        margin: 10,
        marginBottom: 20,
    }

});
