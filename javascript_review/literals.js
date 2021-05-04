/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */
function sides(literals, ...expressions) {
    const width = expressions[0][0];
    const length = expressions[0][1];
    const area = width * length;
    const perimeter = 2 * (width + length);
    const sOne = calculate(true, perimeter, area);
    const sTwo = calculate(false, perimeter, area);
    console.log(sOne, sTwo);
    if(sOne < sTwo){
        return [sOne, sTwo]
    } else {
        return [sTwo, sOne]
    }

}

const calculate = (add, p, a) => 
    add 
        ? (p + Math.sqrt(p ** 2 - 16 * a)) / 4
        : (p - Math.sqrt(p ** 2 - 16 * a)) / 4;


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    // console.log((s1 === x) ? s1 : -1);
    // console.log((s2 === y) ? s2 : -1);
}

sides('', [10, 14]);