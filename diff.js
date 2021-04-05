const diffArray = (arr1, arr2) => {
  const newArr = [];
  arr1.filter(el => arr2.indexOf(el) < 0 && newArr.push(el));
  arr2.filter(element => arr1.indexOf(element) < 0 && newArr.push(element));
  return newArr;
}

//   diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
function destroyer(arr) {
  let allArg = Object.values(arguments);
  const forbidden = allArg.slice(1);
  return arr.filter(el =>
    forbidden.indexOf(el) < 0
  );
}

// console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));

const whatIsInAName = (collection, source) => {
  // Only change code below this line
  const srcKeys = Object.keys(source);
  return collection.filter((obj) => { 
        for(let i = 0; i < srcKeys.length ;i++)
        {
          if(!obj.hasOwnProperty(srcKeys[i]) || obj[srcKeys[i]] !== source[srcKeys[i]]){
            return false;
          }
      };
      return true;
    }
  );
}

// whatIsInAName([{ first: "Romeo", last: "Montague" },
// { first: "Mercutio", last: null },
// { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });
console.log(whatIsInAName([{ "apple": 1, "bat": 2 }, { "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }], { "apple": 1, "bat": 2 }));