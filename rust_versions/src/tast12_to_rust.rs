fn process_digit(digit:i32,operation:i32) -> i32{
    x = operation:i32;
    if let x = None {
        return digit
    }
    return operation(digit)
}
fn zero(operation:i32){
    if operation == None{
        return 0
    }
    return operation
}
fn one(operation:i32){
    if operation == None{
        return 0
    }
    return operation
}
fn plus(n:i32) ->Box<Fn(i32) -> i32>{
    return Box::new(move |n| a + n)
}
