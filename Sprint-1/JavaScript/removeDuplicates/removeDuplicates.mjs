/**
 * Remove duplicate values from a sequence, preserving the order of the first occurrence of each value.
 *
 * Time Complexity: n*n = n^2 = O(n^2)
 * Space Complexity: 1+n = n+1 = O(n)
 * Optimal Time Complexity: n+n = 2n = O(n)
 *
 * @param {Array} inputSequence - Sequence to remove duplicates from
 * @returns {Array} New sequence with duplicates removed
 */
export function removeDuplicates(inputSequence) {
  const uniqueItems = [...new Set(inputSequence)];  // new Set() preserving the order of the inputSequence
  //const uniqueItems = [];

  //for (
  //  let currentIndex = 0;
  //  currentIndex < inputSequence.length;
  //  currentIndex++
  //) {
  //  let isDuplicate = false;
  //  for (
  //    let compareIndex = 0;
  //    compareIndex < uniqueItems.length;
  //    compareIndex++
  //  ) {
  //    if (inputSequence[currentIndex] === uniqueItems[compareIndex]) {
  //      isDuplicate = true;
  //      break;
  //    }
  //  }
  //  if (!isDuplicate) {
  //    uniqueItems.push(inputSequence[currentIndex]);
  //  }
  //}

  return uniqueItems;
}
