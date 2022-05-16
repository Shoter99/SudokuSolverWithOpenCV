import { FlatList, StyleSheet, Text, View } from 'react-native'
import React from 'react'
import GridElement from './GridElement'

const Grid = ({grid, idx, changeValue}) => {
    const numOfColumns = 3
  return (
    <FlatList
        data={grid}
        style={styles.gridContainer}
        renderItem={({ item, index }) => <GridElement changeValue={changeValue} idy={index} idx={idx} num={item}></GridElement>}
        numColumns={numOfColumns}
    />
  )
}

export default Grid

const styles = StyleSheet.create({
    gridContainer: {
        width: '33%',
        borderWidth: 4,
        borderColor: '#00ADB5',
    }
})