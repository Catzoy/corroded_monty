//task9 to rust
//https://www.codewars.com/kata/526571aae218b8ee490006f4/train/rust
//Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
// commented code is for discussion, that's why I left it

pub fn count_bits(n: i64) -> u32 {
    // let mut cnt = n  + 1;
    // let mut tmp = 0;
    // let mut output = vec![];
    // while cnt>=0{
    //     tmp = n & (1<<cnt);
    //         if tmp>0{
    //         output.push(1);
    //     }
    //     else
    //     {
    //         output.push(0);
    //     }
    //     cnt = cnt - 1;
    // }
    // let mut counter:u32 = 0;
    // for i in output {
    //     if i == 1 {
    //         counter += 1;
    //     }
    // }
    // return counter;

    let b = format!("{:b}",n);
    let char_vec: Vec<char> = b.chars().collect();
    let mut counter:u32 = 0;
    for c in char_vec {
        if c == '1'{
            counter += 1;
        }
    }
    return counter
}