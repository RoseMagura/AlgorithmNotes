function reverseString(s) {
    let newString = '';
    try {
        s.split('');
        for(let i = s.length - 1; i >= 0; i--) {
            console.log(s[i]);
            try {
                newString += s[i];
                
            } catch (error) {
                console.log(error);
            }
            
        }
        console.log(newString);
    } catch(error) {
        console.log(error);
    }
}

// reverseString('1234');
reverseString(1234);