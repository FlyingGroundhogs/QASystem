__author__ = 'Hayden'

__name__ = "HandCraftedNER"

class NER:

    stopWords = ['a','an','the','are','as','at','be','by','far','from'
                'has','he','in','is','it','its','on','that','the',
                'to','was','were','will','with', 'when', 'may']

    timeReferences = ['january','february','march','april','may','june','july','august','september','october'
            'november','december','jan','feb','march','apr', 'aug', 'sept', 'oct', 'nov', 'dec', 'today', 'yesterday',
            'o\'clock', 'oclock', 'afternoon', 'evening', 'morning', 'daytime', 'monday', 'tuesday', 'wednesday', 'thursday',
            'friday', 'saturday', 'sunday', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun', 'dawn', 'dusk', 'summer',
            'winter', 'autumn', 'summertime',
            '1700','1701','1702','1703','1704','1705','1706','1707','1708','1709','1710','1711','1712','1713','1714','1715',
            '1716','1717','1718','1719','1720','1721','1722','1723','1724','1725','1726','1727','1728','1729','1730','1731',
            '1732','1733','1734','1735','1736','1737','1738','1739','1740','1741','1742','1743','1744','1745','1746','1747',
            '1748','1749','1750','1751','1752','1753','1754','1755','1756','1757','1758','1759','1760','1761','1762','1763',
            '1764','1765','1766','1767','1768','1769','1770','1771','1772','1773','1774','1775','1776','1777','1778','1779',
            '1780','1781','1782','1783','1784','1785','1786','1787','1788','1789','1790','1791','1792','1793','1794','1795',
            '1796','1797','1798','1799','1800','1801','1802','1803','1804','1805','1806','1807','1808','1809','1810','1811',
            '1812','1813','1814','1815','1816','1817','1818','1819','1820','1821','1822','1823','1824','1825','1826','1827',
            '1828','1829','1830','1831','1832','1833','1834','1835','1836','1837','1838','1839','1840','1841','1842','1843',
            '1844','1845','1846','1847','1848','1849','1850','1851','1852','1853','1854','1855','1856','1857','1858','1859',
            '1860','1861','1862','1863','1864','1865','1866','1867','1868','1869','1870','1871','1872','1873','1874','1875',
            '1876','1877','1878','1879','1880','1881','1882','1883','1884','1885','1886','1887','1888','1889','1890','1891',
            '1892','1893','1894','1895','1896','1897','1898','1899','1900','1901','1902','1903','1904','1905','1906','1907',
            '1908','1909','1910','1911','1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923',
            '1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939',
            '1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955',
            '1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971',
            '1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987',
            '1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003',
            '2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019',
            '2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030']

    locationReferences = ['island', 'mountain', 'mount', 'sound', 'river', 'gulf', 'stream', 'lake', 'ocean', 'sea',
                          'forest', 'pond', 'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado',
                          'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana',
                          'iowa', 'kansas', 'kentucky', 'maine', 'maryland', 'massachusetts', 'ma', 'michigan', 'mississippi',
                          'ms', 'missouri', 'montana', 'nebraska', 'nevada', 'hampshire', 'jersey', 'mexico', 'york', 'carolina',
                          'dakota', 'ohio', 'pennsylvania', 'pa', 'ri', 'rhode', 'carolina', 'america', 'tennessee', 'tn', 'utah'
                          'UT', 'vermont', 'virgina', 'wisconsin', 'washington', 'dc', 'wyoming', 'wy', 'continent', 'isthmus',
                          'africa', 'antarctica', 'brazil', 'europe', 'european', 'african', 'russia', 'asia', 'asian', 'china',
                          'chinese', 'middle', 'south', 'north', 'east', 'south', 'west', 'england', 'office', 'building', 'home',
                          'residence', 'center', 'beach', 'hotel', 'restaurant', 'palace', 'cathedral', 'mine', 'cave',
                          'factory', 'plaza', 'mexico', 'canada', 'mexican', 'canadian', 'calgary', 'toronto', 'alberta',
                          'yukon', 'columbia', 'british', 'manitoba', 'ontario', 'quebec', 'nova', 'new', 'toronto', 'of',
                          'angeles', 'la', 'denver', 'phoenix', 'houston', 'dallas', 'vegas', 'chicago', 'miami', 'detroit',
                          'arctic', 'antarctic', 'subarctic', 'tropics', 'straights', 'hills', 'plains', 'basin']

    groupReferences = ['co', 'corporation', 'llc', 'org', 'brothers', 'partners', 'sisters', 'association', 'organization',
                       'committee', 'assembly', 'consortium', 'google', 'congress', 'government', 'walmart', 'exxon',
                       'chevron', 'berkshire', 'apple', 'motors', 'foundation', 'center', 'group']

    namesGraph = {}
    timesGraph = {}
    def __init__(self, sentence, nameDictionary):

       self.timeArray = []
       self.personArray = []
       self.personOrGroupArray = []
       self.locationArray = []
       self.namesGraph = {}
       self.timesGraph = {}
       self.sentence = sentence
       self.tokens = sentence.split()

       # build the named entity graphs
       self.parseCapitals(self.tokens, 0, 0)
       self.parseTimes(self.tokens, 0, 0)
       self.nameDictionary = nameDictionary

       #proper names can be classified as one of the following: 'PERSON', 'GROUP', 'PERSONORGROUP' 'LOCATION'
       self.personArray = []
       self.groupArray = []
       self.locationArray = []
       self.personOrGroupArray = []

       #append these names to appropriate array(s)
       for  key in self.namesGraph:
           val = self.namesGraph[key]

           personScore = 0
           groupScore = 0
           personOrGroupScore = 0
           locationScore = 0
           temp = ""
           for token in val:
            l = token.lower()
            if nameDictionary.has_key(l):
                personScore +=1
            if l in self.stopWords or l == "of":
                personScore -=1

            if l in self.locationReferences:
                personScore -=1

            if l in self.groupReferences:
                groupScore +=1
            if l in self.locationReferences:
                locationScore +=1


            temp = temp + (token + ' ')


           if personScore >= 1:
            self.personArray.append(temp.strip())

           if groupScore >= 1:
            self.groupArray.append(temp.strip())

           if locationScore >=1:
               self.locationArray.append(temp.strip())

           if personScore is 0 and groupScore is 0:
               self.personOrGroupArray.append(temp.strip())


         #output to times array
       for key in self.timesGraph:
            val = self.timesGraph[key]
            temp = ""
            for token in val:
                l = token.lower()
                temp += l + ' '

            temp = temp.strip()

            self.timeArray.append(temp)




    # we will assume that sequences of capitalized letters are names
    def parseCapitals(self, tokens, tokenIndex, graphIndex):
        if(tokenIndex < len(tokens)  and tokenIndex > -1):
            if(tokenIndex is not 0 and tokens[tokenIndex].lower() not in self.stopWords):
                #check if the token contains an uppercase
                if(any (x.isupper() for x in tokens[tokenIndex])):
                    if self.namesGraph.has_key(graphIndex) is False :
                        self.namesGraph[graphIndex] = []
                    #special case 'of'
                    if(tokenIndex + 1 < len(tokens)):
                        what = tokens[tokenIndex + 1]
                        if(tokens[tokenIndex +1] == "of"):
                            self.namesGraph[graphIndex].append(tokens[tokenIndex])
                            self.namesGraph[graphIndex].append("of")
                            self.parseCapitals(tokens, tokenIndex + 2, graphIndex)
                        else:
                             self.namesGraph[graphIndex].append(tokens[tokenIndex])
                             self.parseCapitals(tokens, tokenIndex + 1, graphIndex)
                    else:
                        self.namesGraph[graphIndex].append(tokens[tokenIndex])
                        self.parseCapitals(tokens, tokenIndex + 1, graphIndex)


                else:
                    self.parseCapitals(tokens, tokenIndex +1, graphIndex+1)
            else:
                self.parseCapitals(tokens, tokenIndex +1, graphIndex+1)
        else:
            x = 32
            #handle special cases here (where the name is the first word of the sentence)


    # look for time related words
    def parseTimes(self, tokens, tokenIndex, graphIndex):
        if(tokenIndex < len(tokens)  and tokenIndex > -1):
            if(tokenIndex is not 0 or tokens[tokenIndex] in  self.timeReferences):
                #check if the token is time related
                if (tokens[tokenIndex].lower() in self.timeReferences):
                    if self.timesGraph.has_key(graphIndex) is False :
                        self.timesGraph[graphIndex] = []
                    self.timesGraph[graphIndex].append(tokens[tokenIndex])
                    self.parseTimes(tokens, tokenIndex + 1, graphIndex)
                else:
                    self.parseTimes(tokens, tokenIndex +1, graphIndex+1)
            else:
                self.parseTimes(tokens, tokenIndex +1, graphIndex+1)


    def printArrays(self):
        print ("HandCrafted NER results for: \"" + self.sentence + "\"")

        print "PERSON:"
        for item in self.personArray:
            print '[' + item + '] ',

        print '\n'
        print "GROUP:"
        for item in self.groupArray:
             print '[' + item + '] ',

        print '\n'
        print "PERSONORGROUP:"
        for item in self.personOrGroupArray:
             print '[' + item + '] ',

        print '\n'
        print "LOCATION:"
        for item in self.locationArray:
            print '[' + item + '] ',

        print '\n'
        print "TIME"
        for item in self.timeArray:
            print '[' + item + '] '

        print
        print '*****************************************************************\n'