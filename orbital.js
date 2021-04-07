const orbitalPeriod = (arr) => {
    for(let index in arr) {
        const current = arr[index];
        const avgAlt = current.avgAlt;
        current['orbitalPeriod'] = calculateOrbital(avgAlt);
        delete current.avgAlt;
    }
    console.log(arr);
    return arr;
  }

const calculateOrbital = (alt) => {
    const GM = 398600.4418;
    const earthRadius = 6367.4447;
    const rawValue = 2 * Math.PI * Math.sqrt( Math.pow(alt + earthRadius, 3) / GM);
    return Math.round(rawValue);
}
  
orbitalPeriod([{name : "sputnik", avgAlt : 35873.5553}]);
orbitalPeriod([{name: "iss", avgAlt: 413.6}, {name: "hubble", avgAlt: 556.7}, {name: "moon", avgAlt: 378632.553}])