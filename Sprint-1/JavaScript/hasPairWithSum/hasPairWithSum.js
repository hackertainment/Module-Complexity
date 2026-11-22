/**
 * Find if there is a pair of numbers that sum to a given target value.
 *
 * Time Complexity: (n-1)+(n-2)+...+1+0 = (n(n-1))/2 = O(n^2)
 * Space Complexity: 1 = 1 = O(1)
 * Optimal Time Complexity: n+n+n = 3n = O(n)
 *
 * @param {Array<number>} numbers - Array of numbers to search through
 * @param {number} target - Target sum to find
 * @returns {boolean} True if pair exists, false otherwise
 */
export function hasPairWithSum(numbers, target) {
  //for (let i = 0; i < numbers.length; i++) {
  //  for (let j = i + 1; j < numbers.length; j++) {
  //    if (numbers[i] + numbers[j] === target) {
  //      return true;
  //    }
  //  }
  //}
  const seen = new Set();
  for (const num of numbers) {
    if (seen.has(target-num)) {  // Set objects must be implemented using either hash tables or ... => O(1) https://262.ecma-international.org/6.0/index.html#sec-set-objects
      return true;
    }
    seen.add(num);
  }
  return false;
}
