fn is_even(num: i32) -> bool {
    return num % 2 == 0;
}

pub fn sort_array(arr: &[i32]) -> Vec<i32> {
    let mut source_array = arr.to_vec();
    let mut evens_counter = 0;
    let mut sorted_odds = source_array.iter().cloned().filter(|&x| !is_even(x)).collect::<Vec<_>>();
    sorted_odds.sort();
    for i in 0..source_array.len(){
        if is_even(source_array[i]){
            evens_counter += 1;
            continue
        }
        source_array[i] = sorted_odds[i - evens_counter];
    }
    return source_array
}

