#!/usr/bin/node
function secondBiggest (nums) {
  if (nums.length <= 1) {
    return 0;
  }
  nums = nums.map(Number).sort((a, b) => b - a);
  return nums[1];
}
const args = process.argv.slice(2);
console.log(secondBiggest(args));
