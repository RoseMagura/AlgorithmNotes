const countingValleys = (steps, path) => {
    let alt = 0; // starting altitude 
    let valley = 0;
    path.forEach(step => {
        step === 'D' 
            ? alt-- 
            : alt++;
        alt === 0 && valley++;
    });
    return valley;
}

countingValleys(8, ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']);