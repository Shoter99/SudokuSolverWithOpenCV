import { SafeAreaView, StyleSheet, Text, View, KeyboardAvoidingView } from 'react-native'
import React from 'react'

export default function AppBar() {
  return (
    <KeyboardAvoidingView behavior="padding" style={styles.container}>
      <Text style={styles.title}>Sudoku Solver</Text>
    </KeyboardAvoidingView>
  )
}

const styles = StyleSheet.create({
    container: {
        margin: 0, 
        padding: 0,
        backgroundColor: '#00ADB5',
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
        color: '#222831'
    }
})