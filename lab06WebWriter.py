# lab06WebWriter.py by Preston Towers for CS20 lab06, 06/07/2016
# Practice with files---this makes a web page from
# the sb2009weather.csv file we used in lab06, or any file in the same format

import os  # This allows access to operating system features

def webDirectory():
    """
    returns a string containing the folder associated with
    web directory http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myHome = os.getenv("HOME")
    if (type(myHome)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return myHome + "/public_html/cs20/lab06"


def webAddress():
    """
    returns the URL (complete with the correct username) for
    http://www.cs.ucsb.edu/~yourusername/cs20/lab06
    """
    
    # Get the home directory

    myUsername = os.getenv("USER")
    if (type(myUsername)!=str):
        
       # raise Exception is a way to force Python to vomit
       # if we've run into a situation we don't know how to handle
       raise Exception("Can't get home directory")

    return "http://www.cs.ucsb.edu/~" + myUsername + "/cs20/lab06"


def makeWebDirectoryIfItDoesNotExistAlready():
    """
    Create the directory ~/public_html/cs20/lab06 unless it already
    exists.
    """
    # This code checks to see if the web directory
    # ~/public_html/cs20/lab06 already exists
    # If so,we just return---there is nothing to do!
    
    if (os.access(webDirectory(),os.F_OK)):
        return

    # If not, then create a web directory for this lab (cs20/lab06)
    # The 0o755 is the Python way or writing octal number 755 (rwxr-xr-x)

    else:
        os.makedirs(webDirectory(),0o755)

        
        
    # If you run this on CSIL, now you should be able to navigate to
    # http://www.cs.ucsb.edu/~yourusername/cs20/lab06 and see files




def webPageHeader(myTitle):
    """
    Returns a string with the head element for a web page
    with title myTitle.
    
    Example: webPageHeader("Temperatures") returns the
    header for a web page with temperatures on it, i.e.
    <head>
      <title>Temperatures</title>
    </head>
    """

    return ("<head>\n" +
      " <title>"+ myTitle + "</title>\n" + 
      "</head>\n")

def makeWeatherWebPage(inputFileName,outputFileName):
    """
    Takes the sb2009weather.csv file we used in an earlier step of the lab
    and converts it into sb2009.html that can be written to the web
    """

    weatherFile = open(inputFileName,"r")

    makeWebDirectoryIfItDoesNotExistAlready()

    htmlFileName = webDirectory() + "/" + outputFileName

    htmlFile = open(htmlFileName,"w")

    htmlFile.write("<html>\n")
    htmlFile.write(webPageHeader("SB Weather"))
    htmlFile.write("<body>\n")
    htmlFile.write("<h1>SB Weather</h1>\n")
    htmlFile.write("<table border='1'>\n")

    htmlFile.write("<tr><th>Date</th><th>Precip (in)</th><th>High</th><th>Low</th><th>Wind Dir</th><th>Wind Speed</th><th>Rel Humid max</th><th>Rel Humid min</th></tr>\n")

    for line in weatherFile:

        lineAsAList = line.strip().split(",")

        date = lineAsAList[0].strip()
        precipIn = lineAsAList[1].strip()
        high = lineAsAList[2].strip()
        low = lineAsAList[3].strip()
        windDir = lineAsAList[4].strip()
        windSpeed = lineAsAList[5].strip()
        relHumidMax = lineAsAList[6].strip()
        relHumidMin = lineAsAList[7].strip()

        htmlFile.write("<tr>" +
                       "<td>" + date + "</td>" +
                       "<td>" + precipIn + "</td>" +
                       "<td>" + high + "</td>" +
                       "<td>" + low + "</td>" +
                       "<td>" + windDir + "</td>" +
                       "<td>" + windSpeed + "</td>" +
                       "<td>" + relHumidMax + "</td>" +
                       "<td>" + relHumidMin + "</td>" +
                       "</tr>")

    htmlFile.write("</table>\n")
    htmlFile.write("</body>\n")
    htmlFile.write("</html>\n")
    
    weatherFile.close()
    htmlFile.close()

    print("Look for the web page at this URL:\n")
    print(" " + webAddress() + "/" + outputFileName)

    print("Or if working on a PC or Mac, at this one:\n")
    print(" file://" + htmlFileName)
