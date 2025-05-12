# https://www.codewars.com/kata/543e926d38603441590021dd/train/python
# Get All Possible Anagrams from a Hash
import itertools
def get_words(hash_of_letters):
    lts = ""
    for c,ls in hash_of_letters.items():
        for l in ls:
            lts += l * c
    _ap = list(itertools.permutations(lts))
    return sorted(set(map(lambda p: "".join(p),_ap)))


#print(get_words({1:["a", "b"]}), ['ab','ba'], "Nope! Try again.")
"""
print(get_words({1:["a", "b", "c", "n", "o"]}), ['abcno', 'abcon', 'abnco', 'abnoc', 'abocn', 
                                                                      'abonc', 'acbno', 'acbon', 'acnbo', 'acnob', 
                                                                      'acobn', 'aconb', 'anbco', 'anboc', 'ancbo', 
                                                                      'ancob', 'anobc', 'anocb', 'aobcn', 'aobnc', 
                                                                      'aocbn', 'aocnb', 'aonbc', 'aoncb', 'bacno', 
                                                                      'bacon', 'banco', 'banoc', 'baocn', 'baonc', 
                                                                      'bcano', 'bcaon', 'bcnao', 'bcnoa', 'bcoan', 
                                                                      'bcona', 'bnaco', 'bnaoc', 'bncao', 'bncoa', 
                                                                      'bnoac', 'bnoca', 'boacn', 'boanc', 'bocan', 
                                                                      'bocna', 'bonac', 'bonca', 'cabno', 'cabon', 
                                                                      'canbo', 'canob', 'caobn', 'caonb', 'cbano', 
                                                                      'cbaon', 'cbnao', 'cbnoa', 'cboan', 'cbona', 
                                                                      'cnabo', 'cnaob', 'cnbao', 'cnboa', 'cnoab', 
                                                                      'cnoba', 'coabn', 'coanb', 'coban', 'cobna', 
                                                                      'conab', 'conba', 'nabco', 'naboc', 'nacbo', 
                                                                      'nacob', 'naobc', 'naocb', 'nbaco', 'nbaoc', 
                                                                      'nbcao', 'nbcoa', 'nboac', 'nboca', 'ncabo', 
                                                                      'ncaob', 'ncbao', 'ncboa', 'ncoab', 'ncoba', 
                                                                      'noabc', 'noacb', 'nobac', 'nobca', 'nocab', 
                                                                      'nocba', 'oabcn', 'oabnc', 'oacbn', 'oacnb', 
                                                                      'oanbc', 'oancb', 'obacn', 'obanc', 'obcan', 
                                                                      'obcna', 'obnac', 'obnca', 'ocabn', 'ocanb', 
                                                                      'ocban', 'ocbna', 'ocnab', 'ocnba', 'onabc', 
                                                                      'onacb', 'onbac', 'onbca', 'oncab', 'oncba'], "Nope! Try again.")
"""        
#print(get_words({1:["a", "b", "c"]}),  ["abc", "acb", "bac", "bca", "cab", "cba"], "Nope! Try again.")
        
print(get_words({2:["a"], 1:["b", "c"]}), ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", 
                                                                "baca", "bcaa", "caab", "caba", "cbaa"], "Nope! Try again.")
"""        
print(get_words({2:["i", "a"], 1:["z","x"]}),  ['aaiixz', 'aaiizx', 'aaixiz', 'aaixzi', 'aaizix', 
                                                                     'aaizxi', 'aaxiiz', 'aaxizi', 'aaxzii', 'aaziix', 'aazixi', 
                                                                     'aazxii', 'aiaixz', 'aiaizx', 'aiaxiz', 'aiaxzi', 'aiazix', 
                                                                     'aiazxi', 'aiiaxz', 'aiiazx', 'aiixaz', 'aiixza', 'aiizax', 
                                                                     'aiizxa', 'aixaiz', 'aixazi', 'aixiaz', 'aixiza', 'aixzai', 
                                                                     'aixzia', 'aizaix', 'aizaxi', 'aiziax', 'aizixa', 'aizxai', 
                                                                     'aizxia', 'axaiiz', 'axaizi', 'axazii', 'axiaiz', 'axiazi', 
                                                                     'axiiaz', 'axiiza', 'axizai', 'axizia', 'axzaii', 'axziai', 
                                                                     'axziia', 'azaiix', 'azaixi', 'azaxii', 'aziaix', 'aziaxi', 
                                                                     'aziiax', 'aziixa', 'azixai', 'azixia', 'azxaii', 'azxiai', 
                                                                     'azxiia', 'iaaixz', 'iaaizx', 'iaaxiz', 'iaaxzi', 'iaazix', 
                                                                     'iaazxi', 'iaiaxz', 'iaiazx', 'iaixaz', 'iaixza', 'iaizax', 
                                                                     'iaizxa', 'iaxaiz', 'iaxazi', 'iaxiaz', 'iaxiza', 'iaxzai', 
                                                                     'iaxzia', 'iazaix', 'iazaxi', 'iaziax', 'iazixa', 'iazxai',
                                                                     'iazxia', 'iiaaxz', 'iiaazx', 'iiaxaz', 'iiaxza', 'iiazax', 
                                                                     'iiazxa', 'iixaaz', 'iixaza', 'iixzaa', 'iizaax', 'iizaxa', 
                                                                     'iizxaa', 'ixaaiz', 'ixaazi', 'ixaiaz', 'ixaiza', 'ixazai', 
                                                                     'ixazia', 'ixiaaz', 'ixiaza', 'ixizaa', 'ixzaai', 'ixzaia', 
                                                                     'ixziaa', 'izaaix', 'izaaxi', 'izaiax', 'izaixa', 'izaxai', 
                                                                     'izaxia', 'iziaax', 'iziaxa', 'izixaa', 'izxaai', 'izxaia', 
                                                                     'izxiaa', 'xaaiiz', 'xaaizi', 'xaazii', 'xaiaiz', 'xaiazi', 
                                                                     'xaiiaz', 'xaiiza', 'xaizai', 'xaizia', 'xazaii', 'xaziai', 
                                                                     'xaziia', 'xiaaiz', 'xiaazi', 'xiaiaz', 'xiaiza', 'xiazai', 
                                                                     'xiazia', 'xiiaaz', 'xiiaza', 'xiizaa', 'xizaai', 'xizaia', 
                                                                     'xiziaa', 'xzaaii', 'xzaiai', 'xzaiia', 'xziaai', 'xziaia', 
                                                                     'xziiaa', 'zaaiix', 'zaaixi', 'zaaxii', 'zaiaix', 'zaiaxi', 
                                                                     'zaiiax', 'zaiixa', 'zaixai', 'zaixia', 'zaxaii', 'zaxiai', 
                                                                     'zaxiia', 'ziaaix', 'ziaaxi', 'ziaiax', 'ziaixa', 'ziaxai', 
                                                                     'ziaxia', 'ziiaax', 'ziiaxa', 'ziixaa', 'zixaai', 'zixaia', 
                                                                     'zixiaa', 'zxaaii', 'zxaiai', 'zxaiia', 'zxiaai', 'zxiaia', 'zxiiaa'], "Nope! Try again.")


"""

#print(list(itertools.permutations('aabc')))