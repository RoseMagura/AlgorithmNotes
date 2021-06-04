const calcFine = (d1, m1, y1, d2, m2, y2) => {
    if (y1 > y2) {
        console.log(10000);
    } else if (y1 < y2) {
        console.log(0);
    }
    else if (m1 > m2) {
        const fine = 500 * (m1 - m2);
        console.log(fine);
    } else if (d1 > d2) {
        const fine = 15 * (d1 - d2);
        console.log(fine);
    } else {
        console.log(0);
    }
}

calcFine(9, 6, 2015, 6, 6, 2015); // should print 45