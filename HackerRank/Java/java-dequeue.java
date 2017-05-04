import java.util.*;

public class test {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Deque deque = new ArrayDeque<>();
        int n = in.nextInt();
        int m = in.nextInt();

        int max = 0;
        int curr = 0;
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int num = in.nextInt();
            if (deque.size() == m) {
                //System.out.print(deque.pollLast());
                int last = (int)deque.pollLast();
                int val = map.get(last) - 1;
                map.put(last, val);
                if (val == 0) {
                    --curr;
                    map.remove(last, val);
                }
            }
            if (!map.containsKey(num) || map.get(num) == 0) {
                ++curr;
            }
            deque.offerFirst(num);
            max = Math.max(max, curr);

            Integer val = map.get(num);
            if (val == null) val = new Integer(0);
            map.put(num, val+1);
        }

        System.out.println(max);
    }
}
