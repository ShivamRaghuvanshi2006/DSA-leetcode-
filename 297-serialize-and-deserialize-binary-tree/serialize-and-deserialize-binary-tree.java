import java.util.*;

public class Codec {

    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeDFS(root, sb);
        return sb.toString();
    }

    private void serializeDFS(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append("#,");
            return;
        }
        sb.append(node.val).append(",");
        serializeDFS(node.left, sb);
        serializeDFS(node.right, sb);
    }

    public TreeNode deserialize(String data) {
        Queue<String> nodes = new LinkedList<>(Arrays.asList(data.split(",")));
        return deserializeDFS(nodes);
    }

    private TreeNode deserializeDFS(Queue<String> nodes) {
        String val = nodes.poll();
        if (val == null || val.equals("#")) {
            return null;
        }

        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = deserializeDFS(nodes);
        node.right = deserializeDFS(nodes);
        return node;
    }
}