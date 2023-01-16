from typing import List
class Solution:

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        pass
    def dfs(node):
        pass
        
    
if __name__=='__main__':
    output=Solution()
    print(output.countSubTrees(4,[[0,1],[1,2],[2,3]],"aaabaaa"))


    """
    TLE
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        list_labels=list(labels)
        origin_labels=list(labels)
        edges_list=edges
        while edges_list:
            
            left,right=zip(*edges_list)
            line_count=list(left)+list(right)
            line_count_set=list(set(line_count))
            
            notfinal=line_count
            for x in line_count_set:
                notfinal.remove(x)

            final=[x for x in range(1,n) if x not in set(notfinal)]
            print(final)
            need_to_remove=[]
            for left_node,right_node in edges_list:
                print('now',[left_node,right_node],'edges_list',edges_list)

                if right_node in final:
                    list_labels[left_node]+=list_labels[right_node]
                    need_to_remove.append([left_node,right_node])

                elif left_node in final:
                    list_labels[right_node]+=list_labels[left_node]
                    need_to_remove.append([left_node,right_node])

            for x in need_to_remove:
                edges_list.remove(x)
            print(edges_list)

        for x in range(n):
            origin_labels[x]=list(list_labels[x]).count(origin_labels[x])

        return origin_labels
    """