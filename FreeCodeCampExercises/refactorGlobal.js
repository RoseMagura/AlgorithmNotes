// The global variable
var bookList = ["The Hound of the Baskervilles", "On The Electrodynamics of Moving Bodies", "Philosophiæ Naturalis Principia Mathematica", "Disquisitiones Arithmeticae"];

// Change code below this line
function add (bookList, bookName) {
  const copy = Array.from(bookList);
  copy.push(bookName);
//   console.log(copy);
  return copy;
  // Change code above this line
}

// Change code below this line
function remove (bookList, bookName) {
  const copy2 = Array.from(bookList);
  var book_index = bookList.indexOf(bookName);
  if (book_index >= 0) {
    copy2.splice(book_index, 1);
    return copy2;
    // Change code above this line
    }
}

var newBookList = add(bookList, 'A Brief History of Time');
// console.log(newBookList);
var newerBookList = remove(bookList, 'On The Electrodynamics of Moving Bodies');
var newestBookList = remove(add(bookList, 'A Brief History of Time'), 'On The Electrodynamics of Moving Bodies');

// console.log(bookList);