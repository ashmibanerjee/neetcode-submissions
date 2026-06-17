class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        key_val_pair={}

        for st in strs:
            print (st)
            key_val_pair[st] = ''.join(sorted(st))
        unique_keys = set(key_val_pair.values())
        unique_key_val_pair = {}
        unique_key_val_pair = {key: [] for key in unique_keys}
 

        for st in strs:
            if ''.join(sorted(st)) in unique_key_val_pair.keys():
                print(st)
                if unique_key_val_pair[''.join(sorted(st))] == []:
                    unique_key_val_pair[''.join(sorted(st))] = [st]
                else:
                    unique_key_val_pair[''.join(sorted(st))].extend([st])
        return list(unique_key_val_pair.values())
  