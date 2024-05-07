# days is a tuple containing the smoke signals and the events that occured
# on a single day. Ex.
# days = [
#   (["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
#   (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
#   (["5.1"],["Orange army retreats"])
#]
def decode_smoke_signals(days):
    shist = dict()
    res = {}
    for day in days:
        for signal in day[0]:
            if signal in shist:
                shist[signal] = shist[signal].intersection(day[1])
            else:
                shist[signal] = set(day[1])
    for s in shist:
        print(shist[s])



    return shist



print(decode_smoke_signals([(["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
            (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
            (["5.1"],["Orange army retreats"])]))




"""
    def moderate():
        test.assert_equals(decode_smoke_signals(
            [(["4","5.1"],["Ambush in the jungle","Orange army retreats"]),
            (["4","5.1","3.2.1"],["Tanks deployed","Orange army retreats","Ambush in the jungle"]),
            (["5.1"],["Orange army retreats"])]
        ),{
            "5.1": "Orange army retreats",
            "4": "Ambush in the jungle",
            "3.2.1": "Tanks deployed"
        })
        
    @test.it("Complex")
    def complex_():
        test.assert_equals(decode_smoke_signals(
            [(["8.2.1","4.3.4","1"],["Ambush in the jungle","General assassinated","Ambush in the jungle"]),
            (["1","2.2","9.3"],["Ambush in the jungle","Orange army retreats","Push into the mountains"]),
            (["4.3.4","6"],["Ambush in the jungle","Orange general goes on vacation"]),
            (["8.2.1","9.3","1"],["Ambush in the jungle","General assassinated","Push into the mountains"])]
        ),{
            "4.3.4": "Ambush in the jungle",
            "6": "Orange general goes on vacation",
            "1": "Ambush in the jungle",
            "8.2.1": "General assassinated",
            "9.3": "Push into the mountains",
            "2.2": "Orange army retreats"
        })
  

"""