const squareList = arr => {
  // Only change code below this line
  const pos = arr.filter(num => num > 0 && num % 1 === 0);
  const squared = pos.map(val => val * val);
  return squared;
  // Only change code above this line
};

// const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
// console.log(squaredIntegers);

const urlSlug = (title) => {
    const lower = title.toLowerCase();
    console.log(lower.split(/\W/).join('-'));
}

urlSlug('Sekiro Shadows Die Twice');