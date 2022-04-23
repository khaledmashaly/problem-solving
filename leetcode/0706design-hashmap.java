// https://leetcode.com/submissions/detail/685725622/

class MyHashMap {
    private static final int BUCKET_COUNT = 1000;

    private final KeyValuePair[] store = new KeyValuePair[BUCKET_COUNT];

    public MyHashMap() {}

    public void put(int key, int value) {
        int bucketIndex = calculateBucketIndex(key);

        if (store[bucketIndex] == null) {
            store[bucketIndex] = new KeyValuePair(key, value);
            return;
        }

        KeyValuePair previous = null;
        KeyValuePair current = store[bucketIndex];

        while (current != null) {
            if (current.key == key) {
                current.value = value;
                return;
            }

            previous = current;
            current = current.next;
        }

        previous.next = new KeyValuePair(key, value);
    }

    public int get(int key) {
        int bucketIndex = calculateBucketIndex(key);

        KeyValuePair current = store[bucketIndex];
        while (current != null) {
            if (current.key == key) {
                return current.value;
            }
            current = current.next;
        }

        return -1;
    }

    public void remove(int key) {
        int bucketIndex = calculateBucketIndex(key);

        if (store[bucketIndex] == null) {
            return;
        }

        if (store[bucketIndex].key == key) {
            store[bucketIndex] = store[bucketIndex].next;
            return;
        }

        KeyValuePair prev = store[bucketIndex];
        KeyValuePair current = store[bucketIndex].next;
        while (current != null) {
            if (current.key == key) {
                prev.next = current.next;
                return;
            }
            prev = current;
            current = current.next;
        }        
    }

    private int calculateBucketIndex(int key) {
        return key % BUCKET_COUNT;
    }

    public static class KeyValuePair {
        private int key;
        private int value;
        private KeyValuePair next;

        public KeyValuePair() {}

        public KeyValuePair(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
}
