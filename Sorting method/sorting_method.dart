void main() {
  // create an unsorted list of integers
  List<int> unsortedList = [3, 6, 2, 8, 1, 5, 9, 4, 7];
  //  call the selectionSort() function to sort unsortedList 
  List<int> sortedList = selectionSort(unsortedList);
  print(sortedList);
}

List<int> selectionSort(List<int> list) {
  for (int i = 0; i < list.length - 1; i++) {
    int minIndex = i;
    for (int j = i + 1; j < list.length; j++) {
      if (list[j] < list[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex != i) {
      int temp = list[i];
      list[i] = list[minIndex];
      list[minIndex] = temp;
    }
  }
  return list;
}
