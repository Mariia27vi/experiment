#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on Май 10, 2026, at 16:37
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'exp'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\Мария Винникова\\Pictures\\Стимулы для экспов с ЭКП\\буквенный массив\\LandT\\stimuli_generated_200\\exp_let_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('resp_vs') is None:
        # initialise resp_vs
        resp_vs = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_vs',
        )
    if deviceManager.getDevice('answ') is None:
        # initialise answ
        answ = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='answ',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('recog_ans') is None:
        # initialise recog_ans
        recog_ans = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='recog_ans',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instr" ---
    text = visual.TextStim(win=win, name='text',
        text='Добрый день!\n\nСпасибо, что согласились принять участие в эксперименте! В процессе прохождения исследования вам необходимо будет запоминать расположение и цвета 4-х квадратов. Далее вам необходимо будет найти на экране букву T и отчитаться о положении буквы в пространстве посредством стрелок <- и ->. Если "хвост буквы Т" (ее нижняя часть) направлен влево, необходимо нажать на стрелку "влево" - <-. Если "хвост буквы Т" (ее нижняя часть) направлен вправо, необходимо нажать на стрелку "вправо"- ->. Далее вам необходимо будет ответить изменилась ли предъявляемая ранее конфигурация цветных квадратов. Если конфигурация не изменилась, нажмите на клавиатуре S (same), если же конфигурация изменилась, нажмите на клавиатуре D (different). \n\nДля продолжения нажмите "ПРОБЕЛ".',
        font='Arial',
        pos=(0, 0), draggable=False, height=25.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "instr_2" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Мы начнем с нескольких тестовых проб в качестве тренировки\n\nВ ходе основной части эксперимента Вам будут давать небольшие перерывы раз в 1-2 мин\n\nПожалуйста, старайтесь выполнять обе задачи с одинаковой эффективностью\n\nЕсли у Вас есть вопросы, задавайте их экспериментатору\n\nНажмите ПРОБЕЛ, чтобы продолжить исследование',
        font='Arial',
        pos=(0, 0), draggable=False, height=25.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "practice_mem" ---
    fix_1 = visual.TextStim(win=win, name='fix_1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    msquare_1 = visual.Rect(
        win=win, name='msquare_1',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    msquare_2 = visual.Rect(
        win=win, name='msquare_2',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    msquare_3 = visual.Rect(
        win=win, name='msquare_3',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    msquare_4 = visual.Rect(
        win=win, name='msquare_4',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    fix_2 = visual.TextStim(win=win, name='fix_2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "vs_2" ---
    image_1 = visual.ImageStim(
        win=win,
        name='image_1', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    resp_vs = keyboard.Keyboard(deviceName='resp_vs')
    
    # --- Initialize components for Routine "fb_vs" ---
    # Run 'Begin Experiment' code from code
    msg=''
    msg_color=''
    feedback_vs = visual.TextStim(win=win, name='feedback_vs',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_recog" ---
    fix = visual.TextStim(win=win, name='fix',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    msquare1 = visual.Rect(
        win=win, name='msquare1',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    msquare2 = visual.Rect(
        win=win, name='msquare2',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    maquare3 = visual.Rect(
        win=win, name='maquare3',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    msquare4 = visual.Rect(
        win=win, name='msquare4',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    answ = keyboard.Keyboard(deviceName='answ')
    
    # --- Initialize components for Routine "fb_recog" ---
    # Run 'Begin Experiment' code from code_2
    mes=''
    mes_color=''
    feedback_memory = visual.TextStim(win=win, name='feedback_memory',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=30.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "pause" ---
    pause_text = visual.TextStim(win=win, name='pause_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "instr_3" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Тестовая часть завершена!\n\nВ основной экспериментальной части обратная связь предъявляться не будет.\n\nПомните, что необходимо нажимать клавишу "S", если положение точки НЕ соответствует одной из ранее предъявленных; клавишу "D", если положение точки соответствует одной из ранее предъявленных. \n\nНажмите ПРОБЕЛ, чтобы перейти к основной части эксперимента.',
        font='Arial',
        pos=(0, 0), draggable=False, height=25.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "memor" ---
    fix1 = visual.TextStim(win=win, name='fix1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    square1 = visual.Rect(
        win=win, name='square1',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    square2 = visual.Rect(
        win=win, name='square2',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    square3 = visual.Rect(
        win=win, name='square3',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    square4 = visual.Rect(
        win=win, name='square4',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    fix2 = visual.TextStim(win=win, name='fix2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "vs_2" ---
    image_1 = visual.ImageStim(
        win=win,
        name='image_1', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    resp_vs = keyboard.Keyboard(deviceName='resp_vs')
    
    # --- Initialize components for Routine "recog" ---
    fix1_1 = visual.TextStim(win=win, name='fix1_1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    square_1 = visual.Rect(
        win=win, name='square_1',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    square_2 = visual.Rect(
        win=win, name='square_2',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    square_3 = visual.Rect(
        win=win, name='square_3',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    square_4 = visual.Rect(
        win=win, name='square_4',
        width=(40, 40)[0], height=(40, 40)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "pause" ---
    pause_text = visual.TextStim(win=win, name='pause_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "instr_4" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Основная часть эксперимента подошла к концу. Половина экранов, которые Вы видели, повторялась в течение эксперимента. Сейчас Вам будет показано 12 экранов, которые повторялись в течение эксперимента, и 12 совершенно новых экранов. \n\nНажмите клавишу со стрелкой, чтобы ответить, предъявлялся ли этот экран ранее: \nстрелка влево (<-), если экран НЕ предъявлялся и Вы видите его впервые;\nстрелка вправо (->), если экран ранее предъявлялся несколько раз в течение эксперимента. \n\nПожалуйста, отвечайте как можно точнее.\n\nНажмите ПРОБЕЛ, чтобы перейти к заданию.',
        font='Arial',
        pos=(0, 0), draggable=False, height=25.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "fix_3" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=50.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "final_recog" ---
    recog_ans = keyboard.Keyboard(deviceName='recog_ans')
    image1 = visual.ImageStim(
        win=win,
        name='image1', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image2 = visual.ImageStim(
        win=win,
        name='image2', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    image3 = visual.ImageStim(
        win=win,
        name='image3', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    image4 = visual.ImageStim(
        win=win,
        name='image4', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    image5 = visual.ImageStim(
        win=win,
        name='image5', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    image6 = visual.ImageStim(
        win=win,
        name='image6', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    image7 = visual.ImageStim(
        win=win,
        name='image7', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    image8 = visual.ImageStim(
        win=win,
        name='image8', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    image9 = visual.ImageStim(
        win=win,
        name='image9', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    image10 = visual.ImageStim(
        win=win,
        name='image10', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    image11 = visual.ImageStim(
        win=win,
        name='image11', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    image12 = visual.ImageStim(
        win=win,
        name='image12', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=[0,0], draggable=False, size=(50, 50),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    
    # --- Initialize components for Routine "end" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Спасибо за участие!\n\nНичего не нажимайте, дождитесь полной загрузки файлов',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instr" ---
    # create an object to store info about Routine instr
    instr = data.Routine(
        name='instr',
        components=[text, key_resp],
    )
    instr.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for instr
    instr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr.tStart = globalClock.getTime(format='float')
    instr.status = STARTED
    thisExp.addData('instr.started', instr.tStart)
    instr.maxDuration = None
    # keep track of which components have finished
    instrComponents = instr.components
    for thisComponent in instr.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr" ---
    instr.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr" ---
    for thisComponent in instr.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr
    instr.tStop = globalClock.getTime(format='float')
    instr.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr.stopped', instr.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr_2" ---
    # create an object to store info about Routine instr_2
    instr_2 = data.Routine(
        name='instr_2',
        components=[text_3, key_resp_2],
    )
    instr_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for instr_2
    instr_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_2.tStart = globalClock.getTime(format='float')
    instr_2.status = STARTED
    thisExp.addData('instr_2.started', instr_2.tStart)
    instr_2.maxDuration = None
    # keep track of which components have finished
    instr_2Components = instr_2.components
    for thisComponent in instr_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_2" ---
    instr_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_2" ---
    for thisComponent in instr_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_2
    instr_2.tStop = globalClock.getTime(format='float')
    instr_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_2.stopped', instr_2.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler2(
        name='practice_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('test_phase_200.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            globals()[paramName] = thisPractice_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_trial in practice_trials:
        practice_trials.status = STARTED
        if hasattr(thisPractice_trial, 'status'):
            thisPractice_trial.status = STARTED
        currentLoop = practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                globals()[paramName] = thisPractice_trial[paramName]
        
        # --- Prepare to start Routine "practice_mem" ---
        # create an object to store info about Routine practice_mem
        practice_mem = data.Routine(
            name='practice_mem',
            components=[fix_1, msquare_1, msquare_2, msquare_3, msquare_4, fix_2],
        )
        practice_mem.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        msquare_1.setFillColor(color_1)
        msquare_1.setPos((pos_sq_x1_1, pos_sq_y1_1))
        msquare_1.setLineColor(color_1)
        msquare_2.setFillColor(color_2)
        msquare_2.setPos((pos_sq_x2_1, pos_sq_y2_1))
        msquare_2.setLineColor(color_2)
        msquare_3.setFillColor(color_3)
        msquare_3.setPos((pos_sq_x3_1, pos_sq_y3_1))
        msquare_3.setLineColor(color_3)
        msquare_4.setFillColor(color_4)
        msquare_4.setPos((pos_sq_x4_1, pos_sq_y4_1))
        msquare_4.setLineColor(color_4)
        # store start times for practice_mem
        practice_mem.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_mem.tStart = globalClock.getTime(format='float')
        practice_mem.status = STARTED
        thisExp.addData('practice_mem.started', practice_mem.tStart)
        practice_mem.maxDuration = None
        # keep track of which components have finished
        practice_memComponents = practice_mem.components
        for thisComponent in practice_mem.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_mem" ---
        practice_mem.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.1:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_1* updates
            
            # if fix_1 is starting this frame...
            if fix_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_1.frameNStart = frameN  # exact frame index
                fix_1.tStart = t  # local t and not account for scr refresh
                fix_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_1.started')
                # update status
                fix_1.status = STARTED
                fix_1.setAutoDraw(True)
            
            # if fix_1 is active this frame...
            if fix_1.status == STARTED:
                # update params
                pass
            
            # if fix_1 is stopping this frame...
            if fix_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_1.tStop = t  # not accounting for scr refresh
                    fix_1.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_1.stopped')
                    # update status
                    fix_1.status = FINISHED
                    fix_1.setAutoDraw(False)
            
            # *msquare_1* updates
            
            # if msquare_1 is starting this frame...
            if msquare_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                msquare_1.frameNStart = frameN  # exact frame index
                msquare_1.tStart = t  # local t and not account for scr refresh
                msquare_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare_1.started')
                # update status
                msquare_1.status = STARTED
                msquare_1.setAutoDraw(True)
            
            # if msquare_1 is active this frame...
            if msquare_1.status == STARTED:
                # update params
                pass
            
            # if msquare_1 is stopping this frame...
            if msquare_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare_1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare_1.tStop = t  # not accounting for scr refresh
                    msquare_1.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare_1.stopped')
                    # update status
                    msquare_1.status = FINISHED
                    msquare_1.setAutoDraw(False)
            
            # *msquare_2* updates
            
            # if msquare_2 is starting this frame...
            if msquare_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                msquare_2.frameNStart = frameN  # exact frame index
                msquare_2.tStart = t  # local t and not account for scr refresh
                msquare_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare_2.started')
                # update status
                msquare_2.status = STARTED
                msquare_2.setAutoDraw(True)
            
            # if msquare_2 is active this frame...
            if msquare_2.status == STARTED:
                # update params
                pass
            
            # if msquare_2 is stopping this frame...
            if msquare_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare_2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare_2.tStop = t  # not accounting for scr refresh
                    msquare_2.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare_2.stopped')
                    # update status
                    msquare_2.status = FINISHED
                    msquare_2.setAutoDraw(False)
            
            # *msquare_3* updates
            
            # if msquare_3 is starting this frame...
            if msquare_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                msquare_3.frameNStart = frameN  # exact frame index
                msquare_3.tStart = t  # local t and not account for scr refresh
                msquare_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare_3.started')
                # update status
                msquare_3.status = STARTED
                msquare_3.setAutoDraw(True)
            
            # if msquare_3 is active this frame...
            if msquare_3.status == STARTED:
                # update params
                pass
            
            # if msquare_3 is stopping this frame...
            if msquare_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare_3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare_3.tStop = t  # not accounting for scr refresh
                    msquare_3.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare_3.stopped')
                    # update status
                    msquare_3.status = FINISHED
                    msquare_3.setAutoDraw(False)
            
            # *msquare_4* updates
            
            # if msquare_4 is starting this frame...
            if msquare_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                msquare_4.frameNStart = frameN  # exact frame index
                msquare_4.tStart = t  # local t and not account for scr refresh
                msquare_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare_4.started')
                # update status
                msquare_4.status = STARTED
                msquare_4.setAutoDraw(True)
            
            # if msquare_4 is active this frame...
            if msquare_4.status == STARTED:
                # update params
                pass
            
            # if msquare_4 is stopping this frame...
            if msquare_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare_4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare_4.tStop = t  # not accounting for scr refresh
                    msquare_4.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare_4.stopped')
                    # update status
                    msquare_4.status = FINISHED
                    msquare_4.setAutoDraw(False)
            
            # *fix_2* updates
            
            # if fix_2 is starting this frame...
            if fix_2.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                fix_2.frameNStart = frameN  # exact frame index
                fix_2.tStart = t  # local t and not account for scr refresh
                fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_2.started')
                # update status
                fix_2.status = STARTED
                fix_2.setAutoDraw(True)
            
            # if fix_2 is active this frame...
            if fix_2.status == STARTED:
                # update params
                pass
            
            # if fix_2 is stopping this frame...
            if fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_2.tStop = t  # not accounting for scr refresh
                    fix_2.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_2.stopped')
                    # update status
                    fix_2.status = FINISHED
                    fix_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_mem,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_mem.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_mem.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_mem" ---
        for thisComponent in practice_mem.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_mem
        practice_mem.tStop = globalClock.getTime(format='float')
        practice_mem.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_mem.stopped', practice_mem.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if practice_mem.maxDurationReached:
            routineTimer.addTime(-practice_mem.maxDuration)
        elif practice_mem.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.100000)
        
        # --- Prepare to start Routine "vs_2" ---
        # create an object to store info about Routine vs_2
        vs_2 = data.Routine(
            name='vs_2',
            components=[image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, image_10, image_11, image_12, resp_vs],
        )
        vs_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        image_1.setPos((posx1, posy1))
        image_1.setOri(orient1)
        image_1.setImage(letter1)
        image_2.setPos((posx2, posy2))
        image_2.setOri(orient2)
        image_2.setImage(letter2)
        image_3.setPos((posx3, posy3))
        image_3.setOri(orient3)
        image_3.setImage(letter3)
        image_4.setPos((posx4, posy4))
        image_4.setOri(orient4)
        image_4.setImage(letter4)
        image_5.setPos((posx5, posy5))
        image_5.setOri(orient5)
        image_5.setImage(letter5)
        image_6.setPos((posx6, posy6))
        image_6.setOri(orient6)
        image_6.setImage(letter6)
        image_7.setPos((posx7, posy7))
        image_7.setOri(orient7)
        image_7.setImage(letter7)
        image_8.setPos((posx8, posy8))
        image_8.setOri(orient8)
        image_8.setImage(letter8)
        image_9.setPos((posx9, posy9))
        image_9.setOri(orient9)
        image_9.setImage(letter9)
        image_10.setPos((posx10, posy10))
        image_10.setOri(orient10)
        image_10.setImage(letter10)
        image_11.setPos((posx11, posy11))
        image_11.setOri(orient11)
        image_11.setImage(letter11)
        image_12.setPos((posx12, posy12))
        image_12.setOri(orient12)
        image_12.setImage(letter12)
        # create starting attributes for resp_vs
        resp_vs.keys = []
        resp_vs.rt = []
        _resp_vs_allKeys = []
        # store start times for vs_2
        vs_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        vs_2.tStart = globalClock.getTime(format='float')
        vs_2.status = STARTED
        thisExp.addData('vs_2.started', vs_2.tStart)
        vs_2.maxDuration = None
        # keep track of which components have finished
        vs_2Components = vs_2.components
        for thisComponent in vs_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "vs_2" ---
        vs_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_1* updates
            
            # if image_1 is starting this frame...
            if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1.frameNStart = frameN  # exact frame index
                image_1.tStart = t  # local t and not account for scr refresh
                image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1.started')
                # update status
                image_1.status = STARTED
                image_1.setAutoDraw(True)
            
            # if image_1 is active this frame...
            if image_1.status == STARTED:
                # update params
                pass
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            
            # *image_7* updates
            
            # if image_7 is starting this frame...
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                # update status
                image_7.status = STARTED
                image_7.setAutoDraw(True)
            
            # if image_7 is active this frame...
            if image_7.status == STARTED:
                # update params
                pass
            
            # *image_8* updates
            
            # if image_8 is starting this frame...
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.started')
                # update status
                image_8.status = STARTED
                image_8.setAutoDraw(True)
            
            # if image_8 is active this frame...
            if image_8.status == STARTED:
                # update params
                pass
            
            # *image_9* updates
            
            # if image_9 is starting this frame...
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.started')
                # update status
                image_9.status = STARTED
                image_9.setAutoDraw(True)
            
            # if image_9 is active this frame...
            if image_9.status == STARTED:
                # update params
                pass
            
            # *image_10* updates
            
            # if image_10 is starting this frame...
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.started')
                # update status
                image_10.status = STARTED
                image_10.setAutoDraw(True)
            
            # if image_10 is active this frame...
            if image_10.status == STARTED:
                # update params
                pass
            
            # *image_11* updates
            
            # if image_11 is starting this frame...
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_11.started')
                # update status
                image_11.status = STARTED
                image_11.setAutoDraw(True)
            
            # if image_11 is active this frame...
            if image_11.status == STARTED:
                # update params
                pass
            
            # *image_12* updates
            
            # if image_12 is starting this frame...
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_12.started')
                # update status
                image_12.status = STARTED
                image_12.setAutoDraw(True)
            
            # if image_12 is active this frame...
            if image_12.status == STARTED:
                # update params
                pass
            
            # *resp_vs* updates
            waitOnFlip = False
            
            # if resp_vs is starting this frame...
            if resp_vs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_vs.frameNStart = frameN  # exact frame index
                resp_vs.tStart = t  # local t and not account for scr refresh
                resp_vs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_vs, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp_vs.started')
                # update status
                resp_vs.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_vs.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_vs.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_vs.status == STARTED and not waitOnFlip:
                theseKeys = resp_vs.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _resp_vs_allKeys.extend(theseKeys)
                if len(_resp_vs_allKeys):
                    resp_vs.keys = _resp_vs_allKeys[-1].name  # just the last key pressed
                    resp_vs.rt = _resp_vs_allKeys[-1].rt
                    resp_vs.duration = _resp_vs_allKeys[-1].duration
                    # was this correct?
                    if (resp_vs.keys == str(direction)) or (resp_vs.keys == direction):
                        resp_vs.corr = 1
                    else:
                        resp_vs.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=vs_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                vs_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vs_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "vs_2" ---
        for thisComponent in vs_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for vs_2
        vs_2.tStop = globalClock.getTime(format='float')
        vs_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('vs_2.stopped', vs_2.tStop)
        # check responses
        if resp_vs.keys in ['', [], None]:  # No response was made
            resp_vs.keys = None
            # was no response the correct answer?!
            if str(direction).lower() == 'none':
               resp_vs.corr = 1;  # correct non-response
            else:
               resp_vs.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('resp_vs.keys',resp_vs.keys)
        practice_trials.addData('resp_vs.corr', resp_vs.corr)
        if resp_vs.keys != None:  # we had a response
            practice_trials.addData('resp_vs.rt', resp_vs.rt)
            practice_trials.addData('resp_vs.duration', resp_vs.duration)
        # the Routine "vs_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fb_vs" ---
        # create an object to store info about Routine fb_vs
        fb_vs = data.Routine(
            name='fb_vs',
            components=[feedback_vs],
        )
        fb_vs.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        if resp_vs.corr==1:
            msg='Правильно'
            msg_color='green'
        else:
            msg='Неправильно'
            msg_color='red'
        feedback_vs.setColor(msg_color, colorSpace='rgb')
        feedback_vs.setText(msg)
        # store start times for fb_vs
        fb_vs.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fb_vs.tStart = globalClock.getTime(format='float')
        fb_vs.status = STARTED
        thisExp.addData('fb_vs.started', fb_vs.tStart)
        fb_vs.maxDuration = None
        # keep track of which components have finished
        fb_vsComponents = fb_vs.components
        for thisComponent in fb_vs.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fb_vs" ---
        fb_vs.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_vs* updates
            
            # if feedback_vs is starting this frame...
            if feedback_vs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_vs.frameNStart = frameN  # exact frame index
                feedback_vs.tStart = t  # local t and not account for scr refresh
                feedback_vs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_vs, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_vs.started')
                # update status
                feedback_vs.status = STARTED
                feedback_vs.setAutoDraw(True)
            
            # if feedback_vs is active this frame...
            if feedback_vs.status == STARTED:
                # update params
                pass
            
            # if feedback_vs is stopping this frame...
            if feedback_vs.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_vs.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_vs.tStop = t  # not accounting for scr refresh
                    feedback_vs.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_vs.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_vs.stopped')
                    # update status
                    feedback_vs.status = FINISHED
                    feedback_vs.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fb_vs,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fb_vs.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fb_vs.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fb_vs" ---
        for thisComponent in fb_vs.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fb_vs
        fb_vs.tStop = globalClock.getTime(format='float')
        fb_vs.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fb_vs.stopped', fb_vs.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fb_vs.maxDurationReached:
            routineTimer.addTime(-fb_vs.maxDuration)
        elif fb_vs.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "practice_recog" ---
        # create an object to store info about Routine practice_recog
        practice_recog = data.Routine(
            name='practice_recog',
            components=[fix, msquare1, msquare2, maquare3, msquare4, answ],
        )
        practice_recog.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        msquare1.setFillColor(color_1)
        msquare1.setPos((pos_sq_x1_1, pos_sq_y1_1))
        msquare1.setLineColor(color_1)
        msquare2.setFillColor(color_2)
        msquare2.setPos((pos_sq_x2_1, pos_sq_y2_1))
        msquare2.setLineColor(color_2)
        maquare3.setFillColor(color_3)
        maquare3.setPos((pos_sq_x3_1, pos_sq_y3_1))
        maquare3.setLineColor(color_3)
        msquare4.setFillColor(color_4)
        msquare4.setPos((pos_sq_x4_1, pos_sq_y4_1))
        msquare4.setLineColor(color_4)
        # create starting attributes for answ
        answ.keys = []
        answ.rt = []
        _answ_allKeys = []
        # store start times for practice_recog
        practice_recog.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_recog.tStart = globalClock.getTime(format='float')
        practice_recog.status = STARTED
        thisExp.addData('practice_recog.started', practice_recog.tStart)
        practice_recog.maxDuration = None
        # keep track of which components have finished
        practice_recogComponents = practice_recog.components
        for thisComponent in practice_recog.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_recog" ---
        practice_recog.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            
            # if fix is starting this frame...
            if fix.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix.started')
                # update status
                fix.status = STARTED
                fix.setAutoDraw(True)
            
            # if fix is active this frame...
            if fix.status == STARTED:
                # update params
                pass
            
            # if fix is stopping this frame...
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.tStopRefresh = tThisFlipGlobal  # on global time
                    fix.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix.stopped')
                    # update status
                    fix.status = FINISHED
                    fix.setAutoDraw(False)
            
            # *msquare1* updates
            
            # if msquare1 is starting this frame...
            if msquare1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                msquare1.frameNStart = frameN  # exact frame index
                msquare1.tStart = t  # local t and not account for scr refresh
                msquare1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare1.started')
                # update status
                msquare1.status = STARTED
                msquare1.setAutoDraw(True)
            
            # if msquare1 is active this frame...
            if msquare1.status == STARTED:
                # update params
                pass
            
            # if msquare1 is stopping this frame...
            if msquare1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare1.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare1.tStop = t  # not accounting for scr refresh
                    msquare1.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare1.stopped')
                    # update status
                    msquare1.status = FINISHED
                    msquare1.setAutoDraw(False)
            
            # *msquare2* updates
            
            # if msquare2 is starting this frame...
            if msquare2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                msquare2.frameNStart = frameN  # exact frame index
                msquare2.tStart = t  # local t and not account for scr refresh
                msquare2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare2.started')
                # update status
                msquare2.status = STARTED
                msquare2.setAutoDraw(True)
            
            # if msquare2 is active this frame...
            if msquare2.status == STARTED:
                # update params
                pass
            
            # if msquare2 is stopping this frame...
            if msquare2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare2.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare2.tStop = t  # not accounting for scr refresh
                    msquare2.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare2.stopped')
                    # update status
                    msquare2.status = FINISHED
                    msquare2.setAutoDraw(False)
            
            # *maquare3* updates
            
            # if maquare3 is starting this frame...
            if maquare3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                maquare3.frameNStart = frameN  # exact frame index
                maquare3.tStart = t  # local t and not account for scr refresh
                maquare3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maquare3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'maquare3.started')
                # update status
                maquare3.status = STARTED
                maquare3.setAutoDraw(True)
            
            # if maquare3 is active this frame...
            if maquare3.status == STARTED:
                # update params
                pass
            
            # if maquare3 is stopping this frame...
            if maquare3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maquare3.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    maquare3.tStop = t  # not accounting for scr refresh
                    maquare3.tStopRefresh = tThisFlipGlobal  # on global time
                    maquare3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'maquare3.stopped')
                    # update status
                    maquare3.status = FINISHED
                    maquare3.setAutoDraw(False)
            
            # *msquare4* updates
            
            # if msquare4 is starting this frame...
            if msquare4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                msquare4.frameNStart = frameN  # exact frame index
                msquare4.tStart = t  # local t and not account for scr refresh
                msquare4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(msquare4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'msquare4.started')
                # update status
                msquare4.status = STARTED
                msquare4.setAutoDraw(True)
            
            # if msquare4 is active this frame...
            if msquare4.status == STARTED:
                # update params
                pass
            
            # if msquare4 is stopping this frame...
            if msquare4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > msquare4.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    msquare4.tStop = t  # not accounting for scr refresh
                    msquare4.tStopRefresh = tThisFlipGlobal  # on global time
                    msquare4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'msquare4.stopped')
                    # update status
                    msquare4.status = FINISHED
                    msquare4.setAutoDraw(False)
            
            # *answ* updates
            waitOnFlip = False
            
            # if answ is starting this frame...
            if answ.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                answ.frameNStart = frameN  # exact frame index
                answ.tStart = t  # local t and not account for scr refresh
                answ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(answ, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'answ.started')
                # update status
                answ.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(answ.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(answ.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if answ.status == STARTED and not waitOnFlip:
                theseKeys = answ.getKeys(keyList=['s','d'], ignoreKeys=["escape"], waitRelease=False)
                _answ_allKeys.extend(theseKeys)
                if len(_answ_allKeys):
                    answ.keys = _answ_allKeys[-1].name  # just the last key pressed
                    answ.rt = _answ_allKeys[-1].rt
                    answ.duration = _answ_allKeys[-1].duration
                    # was this correct?
                    if (answ.keys == str(cor_ans)) or (answ.keys == cor_ans):
                        answ.corr = 1
                    else:
                        answ.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_recog,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_recog.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_recog.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_recog" ---
        for thisComponent in practice_recog.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_recog
        practice_recog.tStop = globalClock.getTime(format='float')
        practice_recog.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_recog.stopped', practice_recog.tStop)
        # check responses
        if answ.keys in ['', [], None]:  # No response was made
            answ.keys = None
            # was no response the correct answer?!
            if str(cor_ans).lower() == 'none':
               answ.corr = 1;  # correct non-response
            else:
               answ.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('answ.keys',answ.keys)
        practice_trials.addData('answ.corr', answ.corr)
        if answ.keys != None:  # we had a response
            practice_trials.addData('answ.rt', answ.rt)
            practice_trials.addData('answ.duration', answ.duration)
        # the Routine "practice_recog" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "fb_recog" ---
        # create an object to store info about Routine fb_recog
        fb_recog = data.Routine(
            name='fb_recog',
            components=[feedback_memory],
        )
        fb_recog.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if answ.corr==1:
            mes='Правильно'
            mes_color='green'
        else:
            mes='Неправильно'
            mes_color='red'
        feedback_memory.setColor(mes_color, colorSpace='rgb')
        feedback_memory.setText(mes)
        # store start times for fb_recog
        fb_recog.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fb_recog.tStart = globalClock.getTime(format='float')
        fb_recog.status = STARTED
        thisExp.addData('fb_recog.started', fb_recog.tStart)
        fb_recog.maxDuration = None
        # keep track of which components have finished
        fb_recogComponents = fb_recog.components
        for thisComponent in fb_recog.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fb_recog" ---
        fb_recog.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_memory* updates
            
            # if feedback_memory is starting this frame...
            if feedback_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_memory.frameNStart = frameN  # exact frame index
                feedback_memory.tStart = t  # local t and not account for scr refresh
                feedback_memory.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_memory, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_memory.started')
                # update status
                feedback_memory.status = STARTED
                feedback_memory.setAutoDraw(True)
            
            # if feedback_memory is active this frame...
            if feedback_memory.status == STARTED:
                # update params
                pass
            
            # if feedback_memory is stopping this frame...
            if feedback_memory.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_memory.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_memory.tStop = t  # not accounting for scr refresh
                    feedback_memory.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_memory.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_memory.stopped')
                    # update status
                    feedback_memory.status = FINISHED
                    feedback_memory.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fb_recog,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fb_recog.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fb_recog.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fb_recog" ---
        for thisComponent in fb_recog.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fb_recog
        fb_recog.tStop = globalClock.getTime(format='float')
        fb_recog.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fb_recog.stopped', fb_recog.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fb_recog.maxDurationReached:
            routineTimer.addTime(-fb_recog.maxDuration)
        elif fb_recog.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "pause" ---
        # create an object to store info about Routine pause
        pause = data.Routine(
            name='pause',
            components=[pause_text],
        )
        pause.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause
        pause.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause.tStart = globalClock.getTime(format='float')
        pause.status = STARTED
        thisExp.addData('pause.started', pause.tStart)
        pause.maxDuration = None
        # keep track of which components have finished
        pauseComponents = pause.components
        for thisComponent in pause.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        pause.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_trial, 'status') and thisPractice_trial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pause_text* updates
            
            # if pause_text is starting this frame...
            if pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pause_text.frameNStart = frameN  # exact frame index
                pause_text.tStart = t  # local t and not account for scr refresh
                pause_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pause_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pause_text.started')
                # update status
                pause_text.status = STARTED
                pause_text.setAutoDraw(True)
            
            # if pause_text is active this frame...
            if pause_text.status == STARTED:
                # update params
                pass
            
            # if pause_text is stopping this frame...
            if pause_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pause_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    pause_text.tStop = t  # not accounting for scr refresh
                    pause_text.tStopRefresh = tThisFlipGlobal  # on global time
                    pause_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pause_text.stopped')
                    # update status
                    pause_text.status = FINISHED
                    pause_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                pause.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pause.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause
        pause.tStop = globalClock.getTime(format='float')
        pause.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause.stopped', pause.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause.maxDurationReached:
            routineTimer.addTime(-pause.maxDuration)
        elif pause.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        # mark thisPractice_trial as finished
        if hasattr(thisPractice_trial, 'status'):
            thisPractice_trial.status = FINISHED
        # if awaiting a pause, pause now
        if practice_trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practice_trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_trials'
    practice_trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instr_3" ---
    # create an object to store info about Routine instr_3
    instr_3 = data.Routine(
        name='instr_3',
        components=[text_4, key_resp_5],
    )
    instr_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # store start times for instr_3
    instr_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_3.tStart = globalClock.getTime(format='float')
    instr_3.status = STARTED
    thisExp.addData('instr_3.started', instr_3.tStart)
    instr_3.maxDuration = None
    # keep track of which components have finished
    instr_3Components = instr_3.components
    for thisComponent in instr_3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_3" ---
    instr_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr_3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_3" ---
    for thisComponent in instr_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_3
    instr_3.tStop = globalClock.getTime(format='float')
    instr_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_3.stopped', instr_3.tStop)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_phase = data.TrialHandler2(
        name='main_phase',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('main_trials_200.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(main_phase)  # add the loop to the experiment
    thisMain_phase = main_phase.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_phase.rgb)
    if thisMain_phase != None:
        for paramName in thisMain_phase:
            globals()[paramName] = thisMain_phase[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_phase in main_phase:
        main_phase.status = STARTED
        if hasattr(thisMain_phase, 'status'):
            thisMain_phase.status = STARTED
        currentLoop = main_phase
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_phase.rgb)
        if thisMain_phase != None:
            for paramName in thisMain_phase:
                globals()[paramName] = thisMain_phase[paramName]
        
        # --- Prepare to start Routine "memor" ---
        # create an object to store info about Routine memor
        memor = data.Routine(
            name='memor',
            components=[fix1, square1, square2, square3, square4, fix2],
        )
        memor.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        square1.setFillColor(color_1)
        square1.setPos((pos_sq_x1_1, pos_sq_y1_1))
        square1.setLineColor(color_1)
        square2.setFillColor(color_2)
        square2.setPos((pos_sq_x2_1, pos_sq_y2_1))
        square2.setLineColor(color_2)
        square3.setFillColor(color_3)
        square3.setPos((pos_sq_x3_1, pos_sq_y3_1))
        square3.setLineColor(color_3)
        square4.setFillColor(color_4)
        square4.setPos((pos_sq_x4_1, pos_sq_y4_1))
        square4.setLineColor(color_4)
        # store start times for memor
        memor.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        memor.tStart = globalClock.getTime(format='float')
        memor.status = STARTED
        thisExp.addData('memor.started', memor.tStart)
        memor.maxDuration = None
        # keep track of which components have finished
        memorComponents = memor.components
        for thisComponent in memor.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "memor" ---
        memor.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.1:
            # if trial has changed, end Routine now
            if hasattr(thisMain_phase, 'status') and thisMain_phase.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix1.started')
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.tStopRefresh = tThisFlipGlobal  # on global time
                    fix1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix1.stopped')
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
            # *square1* updates
            
            # if square1 is starting this frame...
            if square1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square1.frameNStart = frameN  # exact frame index
                square1.tStart = t  # local t and not account for scr refresh
                square1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square1.started')
                # update status
                square1.status = STARTED
                square1.setAutoDraw(True)
            
            # if square1 is active this frame...
            if square1.status == STARTED:
                # update params
                pass
            
            # if square1 is stopping this frame...
            if square1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square1.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    square1.tStop = t  # not accounting for scr refresh
                    square1.tStopRefresh = tThisFlipGlobal  # on global time
                    square1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square1.stopped')
                    # update status
                    square1.status = FINISHED
                    square1.setAutoDraw(False)
            
            # *square2* updates
            
            # if square2 is starting this frame...
            if square2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square2.frameNStart = frameN  # exact frame index
                square2.tStart = t  # local t and not account for scr refresh
                square2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square2.started')
                # update status
                square2.status = STARTED
                square2.setAutoDraw(True)
            
            # if square2 is active this frame...
            if square2.status == STARTED:
                # update params
                pass
            
            # if square2 is stopping this frame...
            if square2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    square2.tStop = t  # not accounting for scr refresh
                    square2.tStopRefresh = tThisFlipGlobal  # on global time
                    square2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square2.stopped')
                    # update status
                    square2.status = FINISHED
                    square2.setAutoDraw(False)
            
            # *square3* updates
            
            # if square3 is starting this frame...
            if square3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square3.frameNStart = frameN  # exact frame index
                square3.tStart = t  # local t and not account for scr refresh
                square3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square3.started')
                # update status
                square3.status = STARTED
                square3.setAutoDraw(True)
            
            # if square3 is active this frame...
            if square3.status == STARTED:
                # update params
                pass
            
            # if square3 is stopping this frame...
            if square3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square3.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    square3.tStop = t  # not accounting for scr refresh
                    square3.tStopRefresh = tThisFlipGlobal  # on global time
                    square3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square3.stopped')
                    # update status
                    square3.status = FINISHED
                    square3.setAutoDraw(False)
            
            # *square4* updates
            
            # if square4 is starting this frame...
            if square4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square4.frameNStart = frameN  # exact frame index
                square4.tStart = t  # local t and not account for scr refresh
                square4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square4.started')
                # update status
                square4.status = STARTED
                square4.setAutoDraw(True)
            
            # if square4 is active this frame...
            if square4.status == STARTED:
                # update params
                pass
            
            # if square4 is stopping this frame...
            if square4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square4.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    square4.tStop = t  # not accounting for scr refresh
                    square4.tStopRefresh = tThisFlipGlobal  # on global time
                    square4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square4.stopped')
                    # update status
                    square4.status = FINISHED
                    square4.setAutoDraw(False)
            
            # *fix2* updates
            
            # if fix2 is starting this frame...
            if fix2.status == NOT_STARTED and tThisFlip >= 0.6-frameTolerance:
                # keep track of start time/frame for later
                fix2.frameNStart = frameN  # exact frame index
                fix2.tStart = t  # local t and not account for scr refresh
                fix2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix2.started')
                # update status
                fix2.status = STARTED
                fix2.setAutoDraw(True)
            
            # if fix2 is active this frame...
            if fix2.status == STARTED:
                # update params
                pass
            
            # if fix2 is stopping this frame...
            if fix2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix2.tStop = t  # not accounting for scr refresh
                    fix2.tStopRefresh = tThisFlipGlobal  # on global time
                    fix2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix2.stopped')
                    # update status
                    fix2.status = FINISHED
                    fix2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=memor,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                memor.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in memor.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "memor" ---
        for thisComponent in memor.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for memor
        memor.tStop = globalClock.getTime(format='float')
        memor.tStopRefresh = tThisFlipGlobal
        thisExp.addData('memor.stopped', memor.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if memor.maxDurationReached:
            routineTimer.addTime(-memor.maxDuration)
        elif memor.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.100000)
        
        # --- Prepare to start Routine "vs_2" ---
        # create an object to store info about Routine vs_2
        vs_2 = data.Routine(
            name='vs_2',
            components=[image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, image_10, image_11, image_12, resp_vs],
        )
        vs_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        image_1.setPos((posx1, posy1))
        image_1.setOri(orient1)
        image_1.setImage(letter1)
        image_2.setPos((posx2, posy2))
        image_2.setOri(orient2)
        image_2.setImage(letter2)
        image_3.setPos((posx3, posy3))
        image_3.setOri(orient3)
        image_3.setImage(letter3)
        image_4.setPos((posx4, posy4))
        image_4.setOri(orient4)
        image_4.setImage(letter4)
        image_5.setPos((posx5, posy5))
        image_5.setOri(orient5)
        image_5.setImage(letter5)
        image_6.setPos((posx6, posy6))
        image_6.setOri(orient6)
        image_6.setImage(letter6)
        image_7.setPos((posx7, posy7))
        image_7.setOri(orient7)
        image_7.setImage(letter7)
        image_8.setPos((posx8, posy8))
        image_8.setOri(orient8)
        image_8.setImage(letter8)
        image_9.setPos((posx9, posy9))
        image_9.setOri(orient9)
        image_9.setImage(letter9)
        image_10.setPos((posx10, posy10))
        image_10.setOri(orient10)
        image_10.setImage(letter10)
        image_11.setPos((posx11, posy11))
        image_11.setOri(orient11)
        image_11.setImage(letter11)
        image_12.setPos((posx12, posy12))
        image_12.setOri(orient12)
        image_12.setImage(letter12)
        # create starting attributes for resp_vs
        resp_vs.keys = []
        resp_vs.rt = []
        _resp_vs_allKeys = []
        # store start times for vs_2
        vs_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        vs_2.tStart = globalClock.getTime(format='float')
        vs_2.status = STARTED
        thisExp.addData('vs_2.started', vs_2.tStart)
        vs_2.maxDuration = None
        # keep track of which components have finished
        vs_2Components = vs_2.components
        for thisComponent in vs_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "vs_2" ---
        vs_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_phase, 'status') and thisMain_phase.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_1* updates
            
            # if image_1 is starting this frame...
            if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_1.frameNStart = frameN  # exact frame index
                image_1.tStart = t  # local t and not account for scr refresh
                image_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1.started')
                # update status
                image_1.status = STARTED
                image_1.setAutoDraw(True)
            
            # if image_1 is active this frame...
            if image_1.status == STARTED:
                # update params
                pass
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            
            # *image_7* updates
            
            # if image_7 is starting this frame...
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_7.started')
                # update status
                image_7.status = STARTED
                image_7.setAutoDraw(True)
            
            # if image_7 is active this frame...
            if image_7.status == STARTED:
                # update params
                pass
            
            # *image_8* updates
            
            # if image_8 is starting this frame...
            if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.started')
                # update status
                image_8.status = STARTED
                image_8.setAutoDraw(True)
            
            # if image_8 is active this frame...
            if image_8.status == STARTED:
                # update params
                pass
            
            # *image_9* updates
            
            # if image_9 is starting this frame...
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.started')
                # update status
                image_9.status = STARTED
                image_9.setAutoDraw(True)
            
            # if image_9 is active this frame...
            if image_9.status == STARTED:
                # update params
                pass
            
            # *image_10* updates
            
            # if image_10 is starting this frame...
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.started')
                # update status
                image_10.status = STARTED
                image_10.setAutoDraw(True)
            
            # if image_10 is active this frame...
            if image_10.status == STARTED:
                # update params
                pass
            
            # *image_11* updates
            
            # if image_11 is starting this frame...
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_11.started')
                # update status
                image_11.status = STARTED
                image_11.setAutoDraw(True)
            
            # if image_11 is active this frame...
            if image_11.status == STARTED:
                # update params
                pass
            
            # *image_12* updates
            
            # if image_12 is starting this frame...
            if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_12.frameNStart = frameN  # exact frame index
                image_12.tStart = t  # local t and not account for scr refresh
                image_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_12.started')
                # update status
                image_12.status = STARTED
                image_12.setAutoDraw(True)
            
            # if image_12 is active this frame...
            if image_12.status == STARTED:
                # update params
                pass
            
            # *resp_vs* updates
            waitOnFlip = False
            
            # if resp_vs is starting this frame...
            if resp_vs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp_vs.frameNStart = frameN  # exact frame index
                resp_vs.tStart = t  # local t and not account for scr refresh
                resp_vs.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_vs, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'resp_vs.started')
                # update status
                resp_vs.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_vs.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_vs.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_vs.status == STARTED and not waitOnFlip:
                theseKeys = resp_vs.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _resp_vs_allKeys.extend(theseKeys)
                if len(_resp_vs_allKeys):
                    resp_vs.keys = _resp_vs_allKeys[-1].name  # just the last key pressed
                    resp_vs.rt = _resp_vs_allKeys[-1].rt
                    resp_vs.duration = _resp_vs_allKeys[-1].duration
                    # was this correct?
                    if (resp_vs.keys == str(direction)) or (resp_vs.keys == direction):
                        resp_vs.corr = 1
                    else:
                        resp_vs.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=vs_2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                vs_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in vs_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "vs_2" ---
        for thisComponent in vs_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for vs_2
        vs_2.tStop = globalClock.getTime(format='float')
        vs_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('vs_2.stopped', vs_2.tStop)
        # check responses
        if resp_vs.keys in ['', [], None]:  # No response was made
            resp_vs.keys = None
            # was no response the correct answer?!
            if str(direction).lower() == 'none':
               resp_vs.corr = 1;  # correct non-response
            else:
               resp_vs.corr = 0;  # failed to respond (incorrectly)
        # store data for main_phase (TrialHandler)
        main_phase.addData('resp_vs.keys',resp_vs.keys)
        main_phase.addData('resp_vs.corr', resp_vs.corr)
        if resp_vs.keys != None:  # we had a response
            main_phase.addData('resp_vs.rt', resp_vs.rt)
            main_phase.addData('resp_vs.duration', resp_vs.duration)
        # the Routine "vs_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "recog" ---
        # create an object to store info about Routine recog
        recog = data.Routine(
            name='recog',
            components=[fix1_1, square_1, square_2, square_3, square_4, key_resp_3],
        )
        recog.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        square_1.setFillColor(color_1)
        square_1.setPos((pos_sq_x1_1, pos_sq_y1_1))
        square_1.setLineColor(color_1)
        square_2.setFillColor(color_2)
        square_2.setPos((pos_sq_x2_1, pos_sq_y2_1))
        square_2.setLineColor(color_2)
        square_3.setFillColor(color_3)
        square_3.setPos((pos_sq_x3_1, pos_sq_y3_1))
        square_3.setLineColor(color_3)
        square_4.setFillColor(color_4)
        square_4.setPos((pos_sq_x4_1, pos_sq_y4_1))
        square_4.setLineColor(color_4)
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # store start times for recog
        recog.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        recog.tStart = globalClock.getTime(format='float')
        recog.status = STARTED
        thisExp.addData('recog.started', recog.tStart)
        recog.maxDuration = None
        # keep track of which components have finished
        recogComponents = recog.components
        for thisComponent in recog.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "recog" ---
        recog.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisMain_phase, 'status') and thisMain_phase.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1_1* updates
            
            # if fix1_1 is starting this frame...
            if fix1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1_1.frameNStart = frameN  # exact frame index
                fix1_1.tStart = t  # local t and not account for scr refresh
                fix1_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix1_1.started')
                # update status
                fix1_1.status = STARTED
                fix1_1.setAutoDraw(True)
            
            # if fix1_1 is active this frame...
            if fix1_1.status == STARTED:
                # update params
                pass
            
            # if fix1_1 is stopping this frame...
            if fix1_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1_1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1_1.tStop = t  # not accounting for scr refresh
                    fix1_1.tStopRefresh = tThisFlipGlobal  # on global time
                    fix1_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix1_1.stopped')
                    # update status
                    fix1_1.status = FINISHED
                    fix1_1.setAutoDraw(False)
            
            # *square_1* updates
            
            # if square_1 is starting this frame...
            if square_1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_1.frameNStart = frameN  # exact frame index
                square_1.tStart = t  # local t and not account for scr refresh
                square_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_1.started')
                # update status
                square_1.status = STARTED
                square_1.setAutoDraw(True)
            
            # if square_1 is active this frame...
            if square_1.status == STARTED:
                # update params
                pass
            
            # if square_1 is stopping this frame...
            if square_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_1.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    square_1.tStop = t  # not accounting for scr refresh
                    square_1.tStopRefresh = tThisFlipGlobal  # on global time
                    square_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_1.stopped')
                    # update status
                    square_1.status = FINISHED
                    square_1.setAutoDraw(False)
            
            # *square_2* updates
            
            # if square_2 is starting this frame...
            if square_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_2.frameNStart = frameN  # exact frame index
                square_2.tStart = t  # local t and not account for scr refresh
                square_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_2.started')
                # update status
                square_2.status = STARTED
                square_2.setAutoDraw(True)
            
            # if square_2 is active this frame...
            if square_2.status == STARTED:
                # update params
                pass
            
            # if square_2 is stopping this frame...
            if square_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_2.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    square_2.tStop = t  # not accounting for scr refresh
                    square_2.tStopRefresh = tThisFlipGlobal  # on global time
                    square_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_2.stopped')
                    # update status
                    square_2.status = FINISHED
                    square_2.setAutoDraw(False)
            
            # *square_3* updates
            
            # if square_3 is starting this frame...
            if square_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_3.frameNStart = frameN  # exact frame index
                square_3.tStart = t  # local t and not account for scr refresh
                square_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_3.started')
                # update status
                square_3.status = STARTED
                square_3.setAutoDraw(True)
            
            # if square_3 is active this frame...
            if square_3.status == STARTED:
                # update params
                pass
            
            # if square_3 is stopping this frame...
            if square_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_3.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    square_3.tStop = t  # not accounting for scr refresh
                    square_3.tStopRefresh = tThisFlipGlobal  # on global time
                    square_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_3.stopped')
                    # update status
                    square_3.status = FINISHED
                    square_3.setAutoDraw(False)
            
            # *square_4* updates
            
            # if square_4 is starting this frame...
            if square_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                square_4.frameNStart = frameN  # exact frame index
                square_4.tStart = t  # local t and not account for scr refresh
                square_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_4.started')
                # update status
                square_4.status = STARTED
                square_4.setAutoDraw(True)
            
            # if square_4 is active this frame...
            if square_4.status == STARTED:
                # update params
                pass
            
            # if square_4 is stopping this frame...
            if square_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > square_4.tStartRefresh + 5.8-frameTolerance:
                    # keep track of stop time/frame for later
                    square_4.tStop = t  # not accounting for scr refresh
                    square_4.tStopRefresh = tThisFlipGlobal  # on global time
                    square_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'square_4.stopped')
                    # update status
                    square_4.status = FINISHED
                    square_4.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['s','d'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_3.keys == str(cor_ans)) or (key_resp_3.keys == cor_ans):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=recog,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                recog.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recog.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recog" ---
        for thisComponent in recog.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for recog
        recog.tStop = globalClock.getTime(format='float')
        recog.tStopRefresh = tThisFlipGlobal
        thisExp.addData('recog.stopped', recog.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(cor_ans).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for main_phase (TrialHandler)
        main_phase.addData('key_resp_3.keys',key_resp_3.keys)
        main_phase.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            main_phase.addData('key_resp_3.rt', key_resp_3.rt)
            main_phase.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "recog" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pause" ---
        # create an object to store info about Routine pause
        pause = data.Routine(
            name='pause',
            components=[pause_text],
        )
        pause.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for pause
        pause.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        pause.tStart = globalClock.getTime(format='float')
        pause.status = STARTED
        thisExp.addData('pause.started', pause.tStart)
        pause.maxDuration = None
        # keep track of which components have finished
        pauseComponents = pause.components
        for thisComponent in pause.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        pause.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisMain_phase, 'status') and thisMain_phase.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pause_text* updates
            
            # if pause_text is starting this frame...
            if pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pause_text.frameNStart = frameN  # exact frame index
                pause_text.tStart = t  # local t and not account for scr refresh
                pause_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pause_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pause_text.started')
                # update status
                pause_text.status = STARTED
                pause_text.setAutoDraw(True)
            
            # if pause_text is active this frame...
            if pause_text.status == STARTED:
                # update params
                pass
            
            # if pause_text is stopping this frame...
            if pause_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pause_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    pause_text.tStop = t  # not accounting for scr refresh
                    pause_text.tStopRefresh = tThisFlipGlobal  # on global time
                    pause_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pause_text.stopped')
                    # update status
                    pause_text.status = FINISHED
                    pause_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=pause,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                pause.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pause.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for pause
        pause.tStop = globalClock.getTime(format='float')
        pause.tStopRefresh = tThisFlipGlobal
        thisExp.addData('pause.stopped', pause.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if pause.maxDurationReached:
            routineTimer.addTime(-pause.maxDuration)
        elif pause.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        # mark thisMain_phase as finished
        if hasattr(thisMain_phase, 'status'):
            thisMain_phase.status = FINISHED
        # if awaiting a pause, pause now
        if main_phase.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            main_phase.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'main_phase'
    main_phase.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instr_4" ---
    # create an object to store info about Routine instr_4
    instr_4 = data.Routine(
        name='instr_4',
        components=[text_5, key_resp_4],
    )
    instr_4.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_4
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # store start times for instr_4
    instr_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instr_4.tStart = globalClock.getTime(format='float')
    instr_4.status = STARTED
    thisExp.addData('instr_4.started', instr_4.tStart)
    instr_4.maxDuration = None
    # keep track of which components have finished
    instr_4Components = instr_4.components
    for thisComponent in instr_4.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instr_4" ---
    instr_4.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instr_4,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instr_4.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_4.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr_4" ---
    for thisComponent in instr_4.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instr_4
    instr_4.tStop = globalClock.getTime(format='float')
    instr_4.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instr_4.stopped', instr_4.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    recognition = data.TrialHandler2(
        name='recognition',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('recog_phase.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(recognition)  # add the loop to the experiment
    thisRecognition = recognition.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecognition.rgb)
    if thisRecognition != None:
        for paramName in thisRecognition:
            globals()[paramName] = thisRecognition[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRecognition in recognition:
        recognition.status = STARTED
        if hasattr(thisRecognition, 'status'):
            thisRecognition.status = STARTED
        currentLoop = recognition
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRecognition.rgb)
        if thisRecognition != None:
            for paramName in thisRecognition:
                globals()[paramName] = thisRecognition[paramName]
        
        # --- Prepare to start Routine "fix_3" ---
        # create an object to store info about Routine fix_3
        fix_3 = data.Routine(
            name='fix_3',
            components=[text_6],
        )
        fix_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fix_3
        fix_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fix_3.tStart = globalClock.getTime(format='float')
        fix_3.status = STARTED
        thisExp.addData('fix_3.started', fix_3.tStart)
        fix_3.maxDuration = None
        # keep track of which components have finished
        fix_3Components = fix_3.components
        for thisComponent in fix_3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fix_3" ---
        fix_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # if trial has changed, end Routine now
            if hasattr(thisRecognition, 'status') and thisRecognition.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # if text_6 is stopping this frame...
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.tStopRefresh = tThisFlipGlobal  # on global time
                    text_6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.stopped')
                    # update status
                    text_6.status = FINISHED
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=fix_3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fix_3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fix_3" ---
        for thisComponent in fix_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fix_3
        fix_3.tStop = globalClock.getTime(format='float')
        fix_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fix_3.stopped', fix_3.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fix_3.maxDurationReached:
            routineTimer.addTime(-fix_3.maxDuration)
        elif fix_3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "final_recog" ---
        # create an object to store info about Routine final_recog
        final_recog = data.Routine(
            name='final_recog',
            components=[recog_ans, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12],
        )
        final_recog.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for recog_ans
        recog_ans.keys = []
        recog_ans.rt = []
        _recog_ans_allKeys = []
        image1.setPos((posx1, posy1))
        image1.setImage(letter1)
        image2.setPos((posx2, posy2))
        image2.setImage(letter2)
        image3.setPos((posx3, posy3))
        image3.setImage(letter3)
        image4.setPos((posx4, posy4))
        image4.setImage(letter4)
        image5.setPos((posx5, posy5))
        image5.setImage(letter5)
        image6.setPos((posx6, posy6))
        image6.setImage(letter6)
        image7.setPos((posx7, posy7))
        image7.setImage(letter7)
        image8.setPos((posx8, posy8))
        image8.setImage(letter8)
        image9.setPos((posx9, posy9))
        image9.setImage(letter9)
        image10.setPos((posx10, posy10))
        image10.setImage(letter10)
        image11.setPos((posx11, posy11))
        image11.setImage(letter11)
        image12.setPos((posx12, posy12))
        image12.setImage(letter12)
        # store start times for final_recog
        final_recog.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        final_recog.tStart = globalClock.getTime(format='float')
        final_recog.status = STARTED
        thisExp.addData('final_recog.started', final_recog.tStart)
        final_recog.maxDuration = None
        # keep track of which components have finished
        final_recogComponents = final_recog.components
        for thisComponent in final_recog.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "final_recog" ---
        final_recog.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisRecognition, 'status') and thisRecognition.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *recog_ans* updates
            waitOnFlip = False
            
            # if recog_ans is starting this frame...
            if recog_ans.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                recog_ans.frameNStart = frameN  # exact frame index
                recog_ans.tStart = t  # local t and not account for scr refresh
                recog_ans.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recog_ans, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recog_ans.started')
                # update status
                recog_ans.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(recog_ans.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(recog_ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if recog_ans.status == STARTED and not waitOnFlip:
                theseKeys = recog_ans.getKeys(keyList=['left','right'], ignoreKeys=["escape"], waitRelease=False)
                _recog_ans_allKeys.extend(theseKeys)
                if len(_recog_ans_allKeys):
                    recog_ans.keys = _recog_ans_allKeys[-1].name  # just the last key pressed
                    recog_ans.rt = _recog_ans_allKeys[-1].rt
                    recog_ans.duration = _recog_ans_allKeys[-1].duration
                    # was this correct?
                    if (recog_ans.keys == str(direction)) or (recog_ans.keys == direction):
                        recog_ans.corr = 1
                    else:
                        recog_ans.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *image1* updates
            
            # if image1 is starting this frame...
            if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1.started')
                # update status
                image1.status = STARTED
                image1.setAutoDraw(True)
            
            # if image1 is active this frame...
            if image1.status == STARTED:
                # update params
                image1.setOri(orient1, log=False)
            
            # *image2* updates
            
            # if image2 is starting this frame...
            if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image2.frameNStart = frameN  # exact frame index
                image2.tStart = t  # local t and not account for scr refresh
                image2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2.started')
                # update status
                image2.status = STARTED
                image2.setAutoDraw(True)
            
            # if image2 is active this frame...
            if image2.status == STARTED:
                # update params
                image2.setOri(orient2, log=False)
            
            # *image3* updates
            
            # if image3 is starting this frame...
            if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image3.frameNStart = frameN  # exact frame index
                image3.tStart = t  # local t and not account for scr refresh
                image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image3.started')
                # update status
                image3.status = STARTED
                image3.setAutoDraw(True)
            
            # if image3 is active this frame...
            if image3.status == STARTED:
                # update params
                image3.setOri(orient3, log=False)
            
            # *image4* updates
            
            # if image4 is starting this frame...
            if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image4.frameNStart = frameN  # exact frame index
                image4.tStart = t  # local t and not account for scr refresh
                image4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image4.started')
                # update status
                image4.status = STARTED
                image4.setAutoDraw(True)
            
            # if image4 is active this frame...
            if image4.status == STARTED:
                # update params
                image4.setOri(orient4, log=False)
            
            # *image5* updates
            
            # if image5 is starting this frame...
            if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image5.frameNStart = frameN  # exact frame index
                image5.tStart = t  # local t and not account for scr refresh
                image5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image5.started')
                # update status
                image5.status = STARTED
                image5.setAutoDraw(True)
            
            # if image5 is active this frame...
            if image5.status == STARTED:
                # update params
                image5.setOri(orient5, log=False)
            
            # *image6* updates
            
            # if image6 is starting this frame...
            if image6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image6.frameNStart = frameN  # exact frame index
                image6.tStart = t  # local t and not account for scr refresh
                image6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image6.started')
                # update status
                image6.status = STARTED
                image6.setAutoDraw(True)
            
            # if image6 is active this frame...
            if image6.status == STARTED:
                # update params
                image6.setOri(orient6, log=False)
            
            # *image7* updates
            
            # if image7 is starting this frame...
            if image7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image7.frameNStart = frameN  # exact frame index
                image7.tStart = t  # local t and not account for scr refresh
                image7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image7.started')
                # update status
                image7.status = STARTED
                image7.setAutoDraw(True)
            
            # if image7 is active this frame...
            if image7.status == STARTED:
                # update params
                image7.setOri(orient7, log=False)
            
            # *image8* updates
            
            # if image8 is starting this frame...
            if image8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image8.frameNStart = frameN  # exact frame index
                image8.tStart = t  # local t and not account for scr refresh
                image8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image8.started')
                # update status
                image8.status = STARTED
                image8.setAutoDraw(True)
            
            # if image8 is active this frame...
            if image8.status == STARTED:
                # update params
                image8.setOri(orient8, log=False)
            
            # *image9* updates
            
            # if image9 is starting this frame...
            if image9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image9.frameNStart = frameN  # exact frame index
                image9.tStart = t  # local t and not account for scr refresh
                image9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image9.started')
                # update status
                image9.status = STARTED
                image9.setAutoDraw(True)
            
            # if image9 is active this frame...
            if image9.status == STARTED:
                # update params
                image9.setOri(orient9, log=False)
            
            # *image10* updates
            
            # if image10 is starting this frame...
            if image10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image10.frameNStart = frameN  # exact frame index
                image10.tStart = t  # local t and not account for scr refresh
                image10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image10.started')
                # update status
                image10.status = STARTED
                image10.setAutoDraw(True)
            
            # if image10 is active this frame...
            if image10.status == STARTED:
                # update params
                image10.setOri(orient10, log=False)
            
            # *image11* updates
            
            # if image11 is starting this frame...
            if image11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image11.frameNStart = frameN  # exact frame index
                image11.tStart = t  # local t and not account for scr refresh
                image11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image11.started')
                # update status
                image11.status = STARTED
                image11.setAutoDraw(True)
            
            # if image11 is active this frame...
            if image11.status == STARTED:
                # update params
                image11.setOri(orient11, log=False)
            
            # *image12* updates
            
            # if image12 is starting this frame...
            if image12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image12.frameNStart = frameN  # exact frame index
                image12.tStart = t  # local t and not account for scr refresh
                image12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image12.started')
                # update status
                image12.status = STARTED
                image12.setAutoDraw(True)
            
            # if image12 is active this frame...
            if image12.status == STARTED:
                # update params
                image12.setOri(orient12, log=False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=final_recog,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                final_recog.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in final_recog.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "final_recog" ---
        for thisComponent in final_recog.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for final_recog
        final_recog.tStop = globalClock.getTime(format='float')
        final_recog.tStopRefresh = tThisFlipGlobal
        thisExp.addData('final_recog.stopped', final_recog.tStop)
        # check responses
        if recog_ans.keys in ['', [], None]:  # No response was made
            recog_ans.keys = None
            # was no response the correct answer?!
            if str(direction).lower() == 'none':
               recog_ans.corr = 1;  # correct non-response
            else:
               recog_ans.corr = 0;  # failed to respond (incorrectly)
        # store data for recognition (TrialHandler)
        recognition.addData('recog_ans.keys',recog_ans.keys)
        recognition.addData('recog_ans.corr', recog_ans.corr)
        if recog_ans.keys != None:  # we had a response
            recognition.addData('recog_ans.rt', recog_ans.rt)
            recognition.addData('recog_ans.duration', recog_ans.duration)
        # the Routine "final_recog" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisRecognition as finished
        if hasattr(thisRecognition, 'status'):
            thisRecognition.status = FINISHED
        # if awaiting a pause, pause now
        if recognition.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            recognition.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'recognition'
    recognition.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[text_2],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=end,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end.maxDurationReached:
        routineTimer.addTime(-end.maxDuration)
    elif end.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
