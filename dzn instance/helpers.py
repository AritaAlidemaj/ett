import json

def getFiek():
    fiek = open('app/fiek.json')
    return json.load(fiek)

def getRooms():
    rooms = open('app/rooms.json')
    return json.load(rooms)

def getPeriods():
    periods = open('app/periods.json')
    return json.load(periods)

def getExams():
    exams = open('app/events.json')
    return json.load(exams)

def getEventRoom():
    eventRoom = open('app/eventRoom.json')
    return json.load(eventRoom)

def getCourses():
    courses = open('app/courses.json')
    return json.load(courses)


def getRoomById(id, roomsData=None):
    roomsList = getRooms() if roomsData is None else roomsData
    for room in roomsList:
        if room['Id'] == id:
            return room
    return None


def getExamById(id, examsData=None):
    examsList = getExams() if examsData is None else examsData
    for exam in examsList:
        if exam['Id'] == id:
            return exam
    return None

def getExamRoom(course):
    eventRooms = getEventRoom()
    for eventRoom in eventRooms:
        if eventRoom['Course'] == course:
            return eventRoom
    return None