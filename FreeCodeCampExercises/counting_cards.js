var count = 0;
function cc(card) {
  // Only change code below this line
  if (card >= 6){
    count++;
  }
  else if (card in [10, 'J', 'Q', 'K', 'A']
) {
    count--;
  }
  
  if (count > 0) {
    return count + ' Bet';
  } else{
  return count + ' Hold';
  }
  // Only change code above this line
}

console.log('HELLO WORLD');
console.log(cc(2)); 
// cc(3); cc(7); cc('K'); cc('A');