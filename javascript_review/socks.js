const sockMerchant = (n, ar) => {
    const sockDict = {};
    let pairs = 0;
    for (let i in ar) {
        if(sockDict[ar[i]] === undefined) {
            sockDict[ar[i]] = 1;
        } else {
            sockDict[ar[i]]++;
            if(sockDict[ar[i]] === 2) {
                pairs++;
                sockDict[ar[i]] = 0;
            } 
        }
    }
    return pairs;
}

sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]); // should return 2
sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]); // should return 3