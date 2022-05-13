import { StyleSheet, Text, View } from 'react-native'
import React from 'react'

const GridElement = ({num}) => {
  return (
    <View style={styles.container}>
      <Text style={{color: 'white'}}>{num || ''}</Text>
    </View>
  )
}

export default GridElement

const styles = StyleSheet.create({
    container: {
        //create border 1px solid white
        borderWidth: 1,
        borderColor: '#fff',
        //create border radius
        borderRadius: 2,
        //create padding
        padding: 10,
        width: '33%',
        alignItems: 'center', 
        justifyContent: 'center',
        fontSize: 28,
        
    }
})