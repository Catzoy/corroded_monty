fn create_sorted_vec(elem:i64) -> Vec<i64>{
    let mut digits = vec![];
    let mut num = elem;
    while num > 9 {
        digits.push(num % 10);
        num = num / 10;
    }
    digits.push(num);
    digits.sort();
    return digits
}
pub fn next_bigger_number(n: i64) -> i64 {
    let digits = create_sorted_vec(n);
    let mut digits1 = create_sorted_vec(n).clone();
    digits1.reverse();
    let mut max_num:i64 = 0;
    for elem in digits1 {
        max_num *= 10;
        max_num += elem;
    }
    let mut output = n;
    while output <= max_num{
          output += 1;
          if create_sorted_vec(output) == digits{
              return output;
          }
      }
    return -1
}