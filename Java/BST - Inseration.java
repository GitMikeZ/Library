static Node Insert(Node root,int value)
{
    Node node = new Node();
    node.data = value;
    node.left = null;
    node.right = null;

    if( root == null )
    {
            root = node;
            return root;
    }
    Node temp = root;
    while( true )
    {
            if( temp.data > value ) {
                    if( temp.left != null ) {
                            temp = temp.left;
                    } else {
                            temp.left = node;
                            break;
                    }
            } else {
                    if( temp.right != null ) {
                            temp = temp.right;
                    } else {
                            temp.right = node;
                            break;
                    }
            }
    }
    return root;
}