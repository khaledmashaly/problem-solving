// https://leetcode.com/submissions/detail/836915227/


class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = Set.of('A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u');
        List<Character> og = new ArrayList<>();
        List<Character> v = new ArrayList<>();

        for (Character c: s.toCharArray()) {
            if (vowels.contains(c)) {
                v.add(c);
                og.add(null);
            }
            else {
                og.add(c);
            }
        }

        int i = v.size() - 1;

        for (int j = 0; j < og.size(); j++) {
            if (og.get(j) == null) {
                og.set(j, v.get(i));
                i--;
            }
        }

        return og.stream()
            .map(String::valueOf)
            .collect(Collectors.joining());
    }
}