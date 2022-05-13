import { SafeAreaView, StyleSheet, Text, View } from 'react-native'
import React from 'react'

export default function AppBar() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Sudoku Solver</Text>
    </View>
  )
}

const styles = StyleSheet.create({
    container: {
        margin: 0, 
        padding: 0,
        backgroundColor: '#eee',
        width: '100%',
        height: '8%',
        justifyContent: 'center',
        padding: 10,
        fontWeight: 'bold',
        borderBottomLeftRadius: 5,
        borderBottomRightRadius: 5,
    },
    title: { 
        fontSize: 20,
    }
})