const pairElement = (str) => {
    let paired = [];
    for(let index in str){
        switch(str[index]) {
            case 'A':
                paired.push(['A', 'T'])
                break;
            case 'T': 
                paired.push(['T', 'A'])
                break;
            case 'G':
                paired.push(['G', 'C'])
                break;
            case 'C':
                paired.push(['C', 'G'])
                break;
        }
    }
    return paired;
}

pairElement('GCG');
