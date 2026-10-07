fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn multiply(a: i32, b: i32) -> i32 {
    a * b
}

fn is_even(n: i32) -> bool {
    n % 2 == 0
}

fn max(a: i32, b: i32) -> i32 {
    if a > b {
        a
    } else {
        b
    }
}

fn square(n: i32) -> i32 {
    n * n
}

fn reverse_string(s: &str) -> String {
    s.chars().rev().collect()
}

fn concat_with_separator(words: &[&str], sep: &str) -> String {
    words.join(sep)
}

fn find_max_in_vec(numbers: &[i32]) -> Option<i32> {
    numbers.iter().copied().max()
}

fn count_evens(numbers: &[i32]) -> usize {
    numbers.iter().filter(|&&n| n % 2 == 0).count()
}

fn main() {
    println!("Week 09: Rust basics");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
        assert_eq!(add(-1, 1), 0);
    }

    #[test]
    fn test_multiply() {
        assert_eq!(multiply(4, 5), 20);
        assert_eq!(multiply(-2, 3), -6);
    }

    #[test]
    fn test_is_even() {
        assert!(is_even(4));
        assert!(!is_even(5));
    }

    #[test]
    fn test_max() {
        assert_eq!(max(10, 5), 10);
        assert_eq!(max(3, 7), 7);
    }

    #[test]
    fn test_square() {
        assert_eq!(square(5), 25);
        assert_eq!(square(-4), 16);
    }

    #[test]
    fn test_reverse_string() {
        assert_eq!(reverse_string("hello"), "olleh");
        assert_eq!(reverse_string("Rust"), "tsuR");
    }

    #[test]
    fn test_concat_with_separator() {
        let words = ["one", "two", "three"];
        assert_eq!(concat_with_separator(&words, ", "), "one, two, three");
    }

    #[test]
    fn test_find_max_in_vec() {
        assert_eq!(find_max_in_vec(&[3, 1, 4, 2]), Some(4));
        assert_eq!(find_max_in_vec(&[]), None);
    }

    #[test]
    fn test_count_evens() {
        assert_eq!(count_evens(&[1, 2, 3, 4, 6]), 3);
        assert_eq!(count_evens(&[1, 3, 5]), 0);
    }
}
