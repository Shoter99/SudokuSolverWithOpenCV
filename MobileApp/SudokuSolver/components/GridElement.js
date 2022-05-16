import { StyleSheet, Text, View, TextInput } from 'react-native'
import React, { useEffect, useState } from 'react'

const GridElement = ({num, idx, idy, changeValue}) => {
  const [value, setValue] = useState(num || '')
  // console.log(num)
  const handleInput = (value) => {
    setValue(value)
    changeValue(idx, idy, value)
  }
  return (
    <View style={styles.container}>
      <TextInput 
        style={{color: 'white', padding: 0, margin: 0}} 
        value={num === " " ? '' : num}
        onChangeText={(text) => {handleInput(text)}}
        keyboardType='numeric'
        maxLength={1}


      />
    </View>
  )
}

export default GridElement

const styles = StyleSheet.create({
    container: {
        //create border 1px solid white
        borderWidth: 1,
        borderColor: '#222831',
        //create border radius
        borderRadius: 2,
        //create padding
        padding: 4,
        width: '33%',
        alignItems: 'center', 
        justifyContent: 'center',
        fontSize: 28,
        
    }
})