/**
 * Finds common items between two arrays.
 *
 * Time Complexity: (n*n)+2n+2n = (n^2)+4n = O(n^2)
 * Space Complexity: n+n+n = 3n = O(n)
 * Optimal Time Complexity: n+n+2n+2n = 6n = O(n)
 *
 * @param {Array} firstArray - First array to compare
 * @param {Array} secondArray - Second array to compare
 * @returns {Array} Array containing unique common items
 */
export const findCommonItems = (firstArray, secondArray) => [
  //...new Set(firstArray.filter((item) => secondArray.includes(item))),
  ...new Set([...firstArray, ...secondArray]);
];
