pub fn generate_hashtag(s:&str) -> String {
    if (s == "") || s.len() > 140{
        return "false".to_string();
    }
    let a:Vec<&str> = s.split(" ").collect::<Vec<_>>();
    let joined = a.join("");
    let mut reverse = joined.chars().rev().collect::<String>();
    reverse.push('#');
    let joined = reverse.chars().rev().collect::<String>();
    return joined;
} 
