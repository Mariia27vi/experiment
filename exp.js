/************ 
 * Exp *
 ************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'exp';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
flowScheduler.add(instr_2RoutineBegin());
flowScheduler.add(instr_2RoutineEachFrame());
flowScheduler.add(instr_2RoutineEnd());
const practice_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_trialsLoopBegin(practice_trialsLoopScheduler));
flowScheduler.add(practice_trialsLoopScheduler);
flowScheduler.add(practice_trialsLoopEnd);







flowScheduler.add(instr_3RoutineBegin());
flowScheduler.add(instr_3RoutineEachFrame());
flowScheduler.add(instr_3RoutineEnd());
const main_phaseLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(main_phaseLoopBegin(main_phaseLoopScheduler));
flowScheduler.add(main_phaseLoopScheduler);
flowScheduler.add(main_phaseLoopEnd);





flowScheduler.add(instr_4RoutineBegin());
flowScheduler.add(instr_4RoutineEachFrame());
flowScheduler.add(instr_4RoutineEnd());
const recognitionLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(recognitionLoopBegin(recognitionLoopScheduler));
flowScheduler.add(recognitionLoopScheduler);
flowScheduler.add(recognitionLoopEnd);



flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'test_phase_200.xlsx', 'path': 'test_phase_200.xlsx'},
    {'name': 'L0.png', 'path': 'L0.png'},
    {'name': 'T0.png', 'path': 'T0.png'},
    {'name': 'main_trials_200.xlsx', 'path': 'main_trials_200.xlsx'},
    {'name': 'L0.png', 'path': 'L0.png'},
    {'name': 'T0.png', 'path': 'T0.png'},
    {'name': 'recog_phase.xlsx', 'path': 'recog_phase.xlsx'},
    {'name': 'L0.png', 'path': 'L0.png'},
    {'name': 'T0.png', 'path': 'T0.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var instrClock;
var text;
var key_resp;
var instr_2Clock;
var text_3;
var key_resp_2;
var practice_memClock;
var fix_1;
var msquare_1;
var msquare_2;
var msquare_3;
var msquare_4;
var fix_2;
var vs_2Clock;
var image_1;
var image_2;
var image_3;
var image_4;
var image_5;
var image_6;
var image_7;
var image_8;
var image_9;
var image_10;
var image_11;
var image_12;
var resp_vs;
var fb_vsClock;
var msg;
var msg_color;
var feedback_vs;
var practice_recogClock;
var fix;
var msquare1;
var msquare2;
var maquare3;
var msquare4;
var answ;
var fb_recogClock;
var mes;
var mes_color;
var feedback_memory;
var pauseClock;
var pause_text;
var instr_3Clock;
var text_4;
var key_resp_5;
var memorClock;
var fix1;
var square1;
var square2;
var square3;
var square4;
var fix2;
var recogClock;
var fix1_1;
var square_1;
var square_2;
var square_3;
var square_4;
var key_resp_3;
var instr_4Clock;
var text_5;
var key_resp_4;
var fix_3Clock;
var text_6;
var final_recogClock;
var recog_ans;
var image1;
var image2;
var image3;
var image4;
var image5;
var image6;
var image7;
var image8;
var image9;
var image10;
var image11;
var image12;
var endClock;
var text_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Добрый день!\n\nСпасибо, что согласились принять участие в эксперименте! В процессе прохождения исследования вам необходимо будет запоминать расположение и цвета 4-х квадратов. Далее вам необходимо будет найти на экране букву T и отчитаться о положении буквы в пространстве посредством стрелок <- и ->. Если "хвост буквы Т" (ее нижняя часть) направлен влево, необходимо нажать на стрелку "влево" - <-. Если "хвост буквы Т" (ее нижняя часть) направлен вправо, необходимо нажать на стрелку "вправо"- ->. Далее вам необходимо будет ответить изменилась ли предъявляемая ранее конфигурация цветных квадратов. Если конфигурация не изменилась, нажмите на клавиатуре S (same), если же конфигурация изменилась, нажмите на клавиатуре D (different). \n\nДля продолжения нажмите "ПРОБЕЛ".',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 25.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_2"
  instr_2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Мы начнем с нескольких тестовых проб в качестве тренировки\n\nВ ходе основной части эксперимента Вам будут давать небольшие перерывы раз в 1-2 мин\n\nПожалуйста, старайтесь выполнять обе задачи с одинаковой эффективностью\n\nЕсли у Вас есть вопросы, задавайте их экспериментатору\n\nНажмите ПРОБЕЛ, чтобы продолжить исследование',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 25.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_mem"
  practice_memClock = new util.Clock();
  fix_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  msquare_1 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare_1', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  msquare_2 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare_2', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  msquare_3 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare_3', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  msquare_4 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare_4', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -4, 
    interpolate: true, 
  });
  
  fix_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "vs_2"
  vs_2Clock = new util.Clock();
  image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  resp_vs = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fb_vs"
  fb_vsClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  msg = "";
  msg_color = "";
  
  feedback_vs = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_vs',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practice_recog"
  practice_recogClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  msquare1 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare1', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  msquare2 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare2', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  maquare3 = new visual.Rect ({
    win: psychoJS.window, name: 'maquare3', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  msquare4 = new visual.Rect ({
    win: psychoJS.window, name: 'msquare4', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -4, 
    interpolate: true, 
  });
  
  answ = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fb_recog"
  fb_recogClock = new util.Clock();
  // Run 'Begin Experiment' code from code_2
  mes = "";
  mes_color = "";
  
  feedback_memory = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_memory',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 30.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  pause_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pause_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instr_3"
  instr_3Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Тестовая часть завершена!\n\nВ основной экспериментальной части обратная связь предъявляться не будет.\n\nПомните, что необходимо нажимать клавишу "S", если положение точки НЕ соответствует одной из ранее предъявленных; клавишу "D", если положение точки соответствует одной из ранее предъявленных. \n\nНажмите ПРОБЕЛ, чтобы перейти к основной части эксперимента.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 25.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "memor"
  memorClock = new util.Clock();
  fix1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  square1 = new visual.Rect ({
    win: psychoJS.window, name: 'square1', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  square2 = new visual.Rect ({
    win: psychoJS.window, name: 'square2', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  square3 = new visual.Rect ({
    win: psychoJS.window, name: 'square3', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  square4 = new visual.Rect ({
    win: psychoJS.window, name: 'square4', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -4, 
    interpolate: true, 
  });
  
  fix2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "recog"
  recogClock = new util.Clock();
  fix1_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix1_1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  square_1 = new visual.Rect ({
    win: psychoJS.window, name: 'square_1', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  square_2 = new visual.Rect ({
    win: psychoJS.window, name: 'square_2', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  square_3 = new visual.Rect ({
    win: psychoJS.window, name: 'square_3', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  square_4 = new visual.Rect ({
    win: psychoJS.window, name: 'square_4', 
    width: [40, 40][0], height: [40, 40][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -4, 
    interpolate: true, 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instr_4"
  instr_4Clock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Основная часть эксперимента подошла к концу. Половина экранов, которые Вы видели, повторялась в течение эксперимента. Сейчас Вам будет показано 12 экранов, которые повторялись в течение эксперимента, и 12 совершенно новых экранов. \n\nНажмите клавишу со стрелкой, чтобы ответить, предъявлялся ли этот экран ранее: \nстрелка влево (<-), если экран НЕ предъявлялся и Вы видите его впервые;\nстрелка вправо (->), если экран ранее предъявлялся несколько раз в течение эксперимента. \n\nПожалуйста, отвечайте как можно точнее.\n\nНажмите ПРОБЕЛ, чтобы перейти к заданию.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 25.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fix_3"
  fix_3Clock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 50.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "final_recog"
  final_recogClock = new util.Clock();
  recog_ans = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  image4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  image5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  image6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image6', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  image7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image7', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  image8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image8', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  image9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image9', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  image10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image10', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  image11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image11', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  image12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image12', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [50, 50],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -12.0 
  });
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Спасибо за участие!\n\nНичего не нажимайте, дождитесь полной загрузки файлов',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var instrMaxDurationReached;
var _key_resp_allKeys;
var instrMaxDuration;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instrClock.reset();
    routineTimer.reset();
    instrMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('instr.started', globalClock.getTime());
    instrMaxDuration = null
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(text);
    instrComponents.push(key_resp);
    
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp* updates
    if (t >= 0.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    // if key_resp is active this frame...
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    for (const thisComponent of instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr_2MaxDurationReached;
var _key_resp_2_allKeys;
var instr_2MaxDuration;
var instr_2Components;
function instr_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_2Clock.reset();
    routineTimer.reset();
    instr_2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('instr_2.started', globalClock.getTime());
    instr_2MaxDuration = null
    // keep track of which components have finished
    instr_2Components = [];
    instr_2Components.push(text_3);
    instr_2Components.push(key_resp_2);
    
    for (const thisComponent of instr_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instr_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_2' ---
    // get current time
    t = instr_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // if text_3 is active this frame...
    if (text_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.5 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    // if key_resp_2 is active this frame...
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_2' ---
    for (const thisComponent of instr_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instr_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_trials;
function practice_trialsLoopBegin(practice_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'test_phase_200.xlsx',
      seed: undefined, name: 'practice_trials'
    });
    psychoJS.experiment.addLoop(practice_trials); // add the loop to the experiment
    currentLoop = practice_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_trial of practice_trials) {
      snapshot = practice_trials.getSnapshot();
      practice_trialsLoopScheduler.add(importConditions(snapshot));
      practice_trialsLoopScheduler.add(practice_memRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(practice_memRoutineEachFrame());
      practice_trialsLoopScheduler.add(practice_memRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(vs_2RoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(vs_2RoutineEachFrame());
      practice_trialsLoopScheduler.add(vs_2RoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(fb_vsRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(fb_vsRoutineEachFrame());
      practice_trialsLoopScheduler.add(fb_vsRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_recogRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(practice_recogRoutineEachFrame());
      practice_trialsLoopScheduler.add(practice_recogRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(fb_recogRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(fb_recogRoutineEachFrame());
      practice_trialsLoopScheduler.add(fb_recogRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(pauseRoutineBegin(snapshot));
      practice_trialsLoopScheduler.add(pauseRoutineEachFrame());
      practice_trialsLoopScheduler.add(pauseRoutineEnd(snapshot));
      practice_trialsLoopScheduler.add(practice_trialsLoopEndIteration(practice_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var main_phase;
function main_phaseLoopBegin(main_phaseLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    main_phase = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'main_trials_200.xlsx',
      seed: undefined, name: 'main_phase'
    });
    psychoJS.experiment.addLoop(main_phase); // add the loop to the experiment
    currentLoop = main_phase;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisMain_phase of main_phase) {
      snapshot = main_phase.getSnapshot();
      main_phaseLoopScheduler.add(importConditions(snapshot));
      main_phaseLoopScheduler.add(memorRoutineBegin(snapshot));
      main_phaseLoopScheduler.add(memorRoutineEachFrame());
      main_phaseLoopScheduler.add(memorRoutineEnd(snapshot));
      main_phaseLoopScheduler.add(vs_2RoutineBegin(snapshot));
      main_phaseLoopScheduler.add(vs_2RoutineEachFrame());
      main_phaseLoopScheduler.add(vs_2RoutineEnd(snapshot));
      main_phaseLoopScheduler.add(recogRoutineBegin(snapshot));
      main_phaseLoopScheduler.add(recogRoutineEachFrame());
      main_phaseLoopScheduler.add(recogRoutineEnd(snapshot));
      main_phaseLoopScheduler.add(pauseRoutineBegin(snapshot));
      main_phaseLoopScheduler.add(pauseRoutineEachFrame());
      main_phaseLoopScheduler.add(pauseRoutineEnd(snapshot));
      main_phaseLoopScheduler.add(main_phaseLoopEndIteration(main_phaseLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function main_phaseLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(main_phase);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function main_phaseLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var recognition;
function recognitionLoopBegin(recognitionLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    recognition = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'recog_phase.xlsx',
      seed: undefined, name: 'recognition'
    });
    psychoJS.experiment.addLoop(recognition); // add the loop to the experiment
    currentLoop = recognition;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRecognition of recognition) {
      snapshot = recognition.getSnapshot();
      recognitionLoopScheduler.add(importConditions(snapshot));
      recognitionLoopScheduler.add(fix_3RoutineBegin(snapshot));
      recognitionLoopScheduler.add(fix_3RoutineEachFrame());
      recognitionLoopScheduler.add(fix_3RoutineEnd(snapshot));
      recognitionLoopScheduler.add(final_recogRoutineBegin(snapshot));
      recognitionLoopScheduler.add(final_recogRoutineEachFrame());
      recognitionLoopScheduler.add(final_recogRoutineEnd(snapshot));
      recognitionLoopScheduler.add(recognitionLoopEndIteration(recognitionLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function recognitionLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(recognition);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function recognitionLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var practice_memMaxDurationReached;
var practice_memMaxDuration;
var practice_memComponents;
function practice_memRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_mem' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practice_memClock.reset(routineTimer.getTime());
    routineTimer.add(1.100000);
    practice_memMaxDurationReached = false;
    // update component parameters for each repeat
    msquare_1.setFillColor(new util.Color(color_1));
    msquare_1.setPos([pos_sq_x1_1, pos_sq_y1_1]);
    msquare_1.setLineColor(new util.Color(color_1));
    msquare_2.setFillColor(new util.Color(color_2));
    msquare_2.setPos([pos_sq_x2_1, pos_sq_y2_1]);
    msquare_2.setLineColor(new util.Color(color_2));
    msquare_3.setFillColor(new util.Color(color_3));
    msquare_3.setPos([pos_sq_x3_1, pos_sq_y3_1]);
    msquare_3.setLineColor(new util.Color(color_3));
    msquare_4.setFillColor(new util.Color(color_4));
    msquare_4.setPos([pos_sq_x4_1, pos_sq_y4_1]);
    msquare_4.setLineColor(new util.Color(color_4));
    psychoJS.experiment.addData('practice_mem.started', globalClock.getTime());
    practice_memMaxDuration = null
    // keep track of which components have finished
    practice_memComponents = [];
    practice_memComponents.push(fix_1);
    practice_memComponents.push(msquare_1);
    practice_memComponents.push(msquare_2);
    practice_memComponents.push(msquare_3);
    practice_memComponents.push(msquare_4);
    practice_memComponents.push(fix_2);
    
    for (const thisComponent of practice_memComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practice_memRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_mem' ---
    // get current time
    t = practice_memClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_1* updates
    if (t >= 0.0 && fix_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_1.tStart = t;  // (not accounting for frame time here)
      fix_1.frameNStart = frameN;  // exact frame index
      
      fix_1.setAutoDraw(true);
    }
    
    
    // if fix_1 is active this frame...
    if (fix_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix_1.tStop = t;  // not accounting for scr refresh
      fix_1.frameNStop = frameN;  // exact frame index
      // update status
      fix_1.status = PsychoJS.Status.FINISHED;
      fix_1.setAutoDraw(false);
    }
    
    
    // *msquare_1* updates
    if (t >= 0.5 && msquare_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare_1.tStart = t;  // (not accounting for frame time here)
      msquare_1.frameNStart = frameN;  // exact frame index
      
      msquare_1.setAutoDraw(true);
    }
    
    
    // if msquare_1 is active this frame...
    if (msquare_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare_1.tStop = t;  // not accounting for scr refresh
      msquare_1.frameNStop = frameN;  // exact frame index
      // update status
      msquare_1.status = PsychoJS.Status.FINISHED;
      msquare_1.setAutoDraw(false);
    }
    
    
    // *msquare_2* updates
    if (t >= 0.5 && msquare_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare_2.tStart = t;  // (not accounting for frame time here)
      msquare_2.frameNStart = frameN;  // exact frame index
      
      msquare_2.setAutoDraw(true);
    }
    
    
    // if msquare_2 is active this frame...
    if (msquare_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare_2.tStop = t;  // not accounting for scr refresh
      msquare_2.frameNStop = frameN;  // exact frame index
      // update status
      msquare_2.status = PsychoJS.Status.FINISHED;
      msquare_2.setAutoDraw(false);
    }
    
    
    // *msquare_3* updates
    if (t >= 0.5 && msquare_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare_3.tStart = t;  // (not accounting for frame time here)
      msquare_3.frameNStart = frameN;  // exact frame index
      
      msquare_3.setAutoDraw(true);
    }
    
    
    // if msquare_3 is active this frame...
    if (msquare_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare_3.tStop = t;  // not accounting for scr refresh
      msquare_3.frameNStop = frameN;  // exact frame index
      // update status
      msquare_3.status = PsychoJS.Status.FINISHED;
      msquare_3.setAutoDraw(false);
    }
    
    
    // *msquare_4* updates
    if (t >= 0.5 && msquare_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare_4.tStart = t;  // (not accounting for frame time here)
      msquare_4.frameNStart = frameN;  // exact frame index
      
      msquare_4.setAutoDraw(true);
    }
    
    
    // if msquare_4 is active this frame...
    if (msquare_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare_4.tStop = t;  // not accounting for scr refresh
      msquare_4.frameNStop = frameN;  // exact frame index
      // update status
      msquare_4.status = PsychoJS.Status.FINISHED;
      msquare_4.setAutoDraw(false);
    }
    
    
    // *fix_2* updates
    if (t >= 0.6 && fix_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_2.tStart = t;  // (not accounting for frame time here)
      fix_2.frameNStart = frameN;  // exact frame index
      
      fix_2.setAutoDraw(true);
    }
    
    
    // if fix_2 is active this frame...
    if (fix_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.6 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix_2.tStop = t;  // not accounting for scr refresh
      fix_2.frameNStop = frameN;  // exact frame index
      // update status
      fix_2.status = PsychoJS.Status.FINISHED;
      fix_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_memComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_memRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_mem' ---
    for (const thisComponent of practice_memComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_mem.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (practice_memMaxDurationReached) {
        practice_memClock.add(practice_memMaxDuration);
    } else {
        practice_memClock.add(1.100000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var vs_2MaxDurationReached;
var _resp_vs_allKeys;
var vs_2MaxDuration;
var vs_2Components;
function vs_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'vs_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    vs_2Clock.reset();
    routineTimer.reset();
    vs_2MaxDurationReached = false;
    // update component parameters for each repeat
    image_1.setPos([posx1, posy1]);
    image_1.setOri(orient1);
    image_1.setImage(letter1);
    image_2.setPos([posx2, posy2]);
    image_2.setOri(orient2);
    image_2.setImage(letter2);
    image_3.setPos([posx3, posy3]);
    image_3.setOri(orient3);
    image_3.setImage(letter3);
    image_4.setPos([posx4, posy4]);
    image_4.setOri(orient4);
    image_4.setImage(letter4);
    image_5.setPos([posx5, posy5]);
    image_5.setOri(orient5);
    image_5.setImage(letter5);
    image_6.setPos([posx6, posy6]);
    image_6.setOri(orient6);
    image_6.setImage(letter6);
    image_7.setPos([posx7, posy7]);
    image_7.setOri(orient7);
    image_7.setImage(letter7);
    image_8.setPos([posx8, posy8]);
    image_8.setOri(orient8);
    image_8.setImage(letter8);
    image_9.setPos([posx9, posy9]);
    image_9.setOri(orient9);
    image_9.setImage(letter9);
    image_10.setPos([posx10, posy10]);
    image_10.setOri(orient10);
    image_10.setImage(letter10);
    image_11.setPos([posx11, posy11]);
    image_11.setOri(orient11);
    image_11.setImage(letter11);
    image_12.setPos([posx12, posy12]);
    image_12.setOri(orient12);
    image_12.setImage(letter12);
    resp_vs.keys = undefined;
    resp_vs.rt = undefined;
    _resp_vs_allKeys = [];
    psychoJS.experiment.addData('vs_2.started', globalClock.getTime());
    vs_2MaxDuration = null
    // keep track of which components have finished
    vs_2Components = [];
    vs_2Components.push(image_1);
    vs_2Components.push(image_2);
    vs_2Components.push(image_3);
    vs_2Components.push(image_4);
    vs_2Components.push(image_5);
    vs_2Components.push(image_6);
    vs_2Components.push(image_7);
    vs_2Components.push(image_8);
    vs_2Components.push(image_9);
    vs_2Components.push(image_10);
    vs_2Components.push(image_11);
    vs_2Components.push(image_12);
    vs_2Components.push(resp_vs);
    
    for (const thisComponent of vs_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function vs_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'vs_2' ---
    // get current time
    t = vs_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_1* updates
    if (t >= 0.0 && image_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_1.tStart = t;  // (not accounting for frame time here)
      image_1.frameNStart = frameN;  // exact frame index
      
      image_1.setAutoDraw(true);
    }
    
    
    // if image_1 is active this frame...
    if (image_1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    
    // if image_2 is active this frame...
    if (image_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    
    // if image_3 is active this frame...
    if (image_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    
    // if image_4 is active this frame...
    if (image_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }
    
    
    // if image_5 is active this frame...
    if (image_5.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_6* updates
    if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }
    
    
    // if image_6 is active this frame...
    if (image_6.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_7* updates
    if (t >= 0.0 && image_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_7.tStart = t;  // (not accounting for frame time here)
      image_7.frameNStart = frameN;  // exact frame index
      
      image_7.setAutoDraw(true);
    }
    
    
    // if image_7 is active this frame...
    if (image_7.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_8* updates
    if (t >= 0.0 && image_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_8.tStart = t;  // (not accounting for frame time here)
      image_8.frameNStart = frameN;  // exact frame index
      
      image_8.setAutoDraw(true);
    }
    
    
    // if image_8 is active this frame...
    if (image_8.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_9* updates
    if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index
      
      image_9.setAutoDraw(true);
    }
    
    
    // if image_9 is active this frame...
    if (image_9.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_10* updates
    if (t >= 0.0 && image_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_10.tStart = t;  // (not accounting for frame time here)
      image_10.frameNStart = frameN;  // exact frame index
      
      image_10.setAutoDraw(true);
    }
    
    
    // if image_10 is active this frame...
    if (image_10.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }
    
    
    // if image_11 is active this frame...
    if (image_11.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_12* updates
    if (t >= 0.0 && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index
      
      image_12.setAutoDraw(true);
    }
    
    
    // if image_12 is active this frame...
    if (image_12.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *resp_vs* updates
    if (t >= 0.0 && resp_vs.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_vs.tStart = t;  // (not accounting for frame time here)
      resp_vs.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_vs.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_vs.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_vs.clearEvents(); });
    }
    
    // if resp_vs is active this frame...
    if (resp_vs.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_vs.getKeys({keyList: ['left','right'], waitRelease: false});
      _resp_vs_allKeys = _resp_vs_allKeys.concat(theseKeys);
      if (_resp_vs_allKeys.length > 0) {
        resp_vs.keys = _resp_vs_allKeys[_resp_vs_allKeys.length - 1].name;  // just the last key pressed
        resp_vs.rt = _resp_vs_allKeys[_resp_vs_allKeys.length - 1].rt;
        resp_vs.duration = _resp_vs_allKeys[_resp_vs_allKeys.length - 1].duration;
        // was this correct?
        if (resp_vs.keys == direction) {
            resp_vs.corr = 1;
        } else {
            resp_vs.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of vs_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function vs_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'vs_2' ---
    for (const thisComponent of vs_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('vs_2.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (resp_vs.keys === undefined) {
      if (['None','none',undefined].includes(direction)) {
         resp_vs.corr = 1;  // correct non-response
      } else {
         resp_vs.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_vs.corr, level);
    }
    psychoJS.experiment.addData('resp_vs.keys', resp_vs.keys);
    psychoJS.experiment.addData('resp_vs.corr', resp_vs.corr);
    if (typeof resp_vs.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_vs.rt', resp_vs.rt);
        psychoJS.experiment.addData('resp_vs.duration', resp_vs.duration);
        routineTimer.reset();
        }
    
    resp_vs.stop();
    // the Routine "vs_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fb_vsMaxDurationReached;
var fb_vsMaxDuration;
var fb_vsComponents;
function fb_vsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fb_vs' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fb_vsClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    fb_vsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    if ((resp_vs.corr === 1)) {
        msg = "\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e";
        msg_color = "green";
    } else {
        msg = "\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e";
        msg_color = "red";
    }
    
    feedback_vs.setColor(new util.Color(msg_color));
    feedback_vs.setText(msg);
    psychoJS.experiment.addData('fb_vs.started', globalClock.getTime());
    fb_vsMaxDuration = null
    // keep track of which components have finished
    fb_vsComponents = [];
    fb_vsComponents.push(feedback_vs);
    
    for (const thisComponent of fb_vsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fb_vsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fb_vs' ---
    // get current time
    t = fb_vsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_vs* updates
    if (t >= 0.0 && feedback_vs.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_vs.tStart = t;  // (not accounting for frame time here)
      feedback_vs.frameNStart = frameN;  // exact frame index
      
      feedback_vs.setAutoDraw(true);
    }
    
    
    // if feedback_vs is active this frame...
    if (feedback_vs.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_vs.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      feedback_vs.tStop = t;  // not accounting for scr refresh
      feedback_vs.frameNStop = frameN;  // exact frame index
      // update status
      feedback_vs.status = PsychoJS.Status.FINISHED;
      feedback_vs.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fb_vsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_vsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fb_vs' ---
    for (const thisComponent of fb_vsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fb_vs.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fb_vsMaxDurationReached) {
        fb_vsClock.add(fb_vsMaxDuration);
    } else {
        fb_vsClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_recogMaxDurationReached;
var _answ_allKeys;
var practice_recogMaxDuration;
var practice_recogComponents;
function practice_recogRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_recog' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practice_recogClock.reset();
    routineTimer.reset();
    practice_recogMaxDurationReached = false;
    // update component parameters for each repeat
    msquare1.setFillColor(new util.Color(color_1));
    msquare1.setPos([pos_sq_x1_1, pos_sq_y1_1]);
    msquare1.setLineColor(new util.Color(color_1));
    msquare2.setFillColor(new util.Color(color_2));
    msquare2.setPos([pos_sq_x2_1, pos_sq_y2_1]);
    msquare2.setLineColor(new util.Color(color_2));
    maquare3.setFillColor(new util.Color(color_3));
    maquare3.setPos([pos_sq_x3_1, pos_sq_y3_1]);
    maquare3.setLineColor(new util.Color(color_3));
    msquare4.setFillColor(new util.Color(color_4));
    msquare4.setPos([pos_sq_x4_1, pos_sq_y4_1]);
    msquare4.setLineColor(new util.Color(color_4));
    answ.keys = undefined;
    answ.rt = undefined;
    _answ_allKeys = [];
    psychoJS.experiment.addData('practice_recog.started', globalClock.getTime());
    practice_recogMaxDuration = null
    // keep track of which components have finished
    practice_recogComponents = [];
    practice_recogComponents.push(fix);
    practice_recogComponents.push(msquare1);
    practice_recogComponents.push(msquare2);
    practice_recogComponents.push(maquare3);
    practice_recogComponents.push(msquare4);
    practice_recogComponents.push(answ);
    
    for (const thisComponent of practice_recogComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_recogRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_recog' ---
    // get current time
    t = practice_recogClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.5 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }
    
    
    // if fix is active this frame...
    if (fix.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix.tStop = t;  // not accounting for scr refresh
      fix.frameNStop = frameN;  // exact frame index
      // update status
      fix.status = PsychoJS.Status.FINISHED;
      fix.setAutoDraw(false);
    }
    
    
    // *msquare1* updates
    if (t >= 1.0 && msquare1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare1.tStart = t;  // (not accounting for frame time here)
      msquare1.frameNStart = frameN;  // exact frame index
      
      msquare1.setAutoDraw(true);
    }
    
    
    // if msquare1 is active this frame...
    if (msquare1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1.0 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare1.tStop = t;  // not accounting for scr refresh
      msquare1.frameNStop = frameN;  // exact frame index
      // update status
      msquare1.status = PsychoJS.Status.FINISHED;
      msquare1.setAutoDraw(false);
    }
    
    
    // *msquare2* updates
    if (t >= 1.0 && msquare2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare2.tStart = t;  // (not accounting for frame time here)
      msquare2.frameNStart = frameN;  // exact frame index
      
      msquare2.setAutoDraw(true);
    }
    
    
    // if msquare2 is active this frame...
    if (msquare2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1.0 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare2.tStop = t;  // not accounting for scr refresh
      msquare2.frameNStop = frameN;  // exact frame index
      // update status
      msquare2.status = PsychoJS.Status.FINISHED;
      msquare2.setAutoDraw(false);
    }
    
    
    // *maquare3* updates
    if (t >= 1.0 && maquare3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      maquare3.tStart = t;  // (not accounting for frame time here)
      maquare3.frameNStart = frameN;  // exact frame index
      
      maquare3.setAutoDraw(true);
    }
    
    
    // if maquare3 is active this frame...
    if (maquare3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1.0 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (maquare3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      maquare3.tStop = t;  // not accounting for scr refresh
      maquare3.frameNStop = frameN;  // exact frame index
      // update status
      maquare3.status = PsychoJS.Status.FINISHED;
      maquare3.setAutoDraw(false);
    }
    
    
    // *msquare4* updates
    if (t >= 1.0 && msquare4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      msquare4.tStart = t;  // (not accounting for frame time here)
      msquare4.frameNStart = frameN;  // exact frame index
      
      msquare4.setAutoDraw(true);
    }
    
    
    // if msquare4 is active this frame...
    if (msquare4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 1.0 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (msquare4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      msquare4.tStop = t;  // not accounting for scr refresh
      msquare4.frameNStop = frameN;  // exact frame index
      // update status
      msquare4.status = PsychoJS.Status.FINISHED;
      msquare4.setAutoDraw(false);
    }
    
    
    // *answ* updates
    if (t >= 1.0 && answ.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answ.tStart = t;  // (not accounting for frame time here)
      answ.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { answ.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { answ.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { answ.clearEvents(); });
    }
    
    // if answ is active this frame...
    if (answ.status === PsychoJS.Status.STARTED) {
      let theseKeys = answ.getKeys({keyList: ['s','d'], waitRelease: false});
      _answ_allKeys = _answ_allKeys.concat(theseKeys);
      if (_answ_allKeys.length > 0) {
        answ.keys = _answ_allKeys[_answ_allKeys.length - 1].name;  // just the last key pressed
        answ.rt = _answ_allKeys[_answ_allKeys.length - 1].rt;
        answ.duration = _answ_allKeys[_answ_allKeys.length - 1].duration;
        // was this correct?
        if (answ.keys == cor_ans) {
            answ.corr = 1;
        } else {
            answ.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_recogComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_recogRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_recog' ---
    for (const thisComponent of practice_recogComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('practice_recog.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (answ.keys === undefined) {
      if (['None','none',undefined].includes(cor_ans)) {
         answ.corr = 1;  // correct non-response
      } else {
         answ.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(answ.corr, level);
    }
    psychoJS.experiment.addData('answ.keys', answ.keys);
    psychoJS.experiment.addData('answ.corr', answ.corr);
    if (typeof answ.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('answ.rt', answ.rt);
        psychoJS.experiment.addData('answ.duration', answ.duration);
        routineTimer.reset();
        }
    
    answ.stop();
    // the Routine "practice_recog" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fb_recogMaxDurationReached;
var fb_recogMaxDuration;
var fb_recogComponents;
function fb_recogRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fb_recog' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fb_recogClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    fb_recogMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    if ((answ.corr === 1)) {
        mes = "\u041f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e";
        mes_color = "green";
    } else {
        mes = "\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e";
        mes_color = "red";
    }
    
    feedback_memory.setColor(new util.Color(mes_color));
    feedback_memory.setText(mes);
    psychoJS.experiment.addData('fb_recog.started', globalClock.getTime());
    fb_recogMaxDuration = null
    // keep track of which components have finished
    fb_recogComponents = [];
    fb_recogComponents.push(feedback_memory);
    
    for (const thisComponent of fb_recogComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fb_recogRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fb_recog' ---
    // get current time
    t = fb_recogClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_memory* updates
    if (t >= 0.0 && feedback_memory.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_memory.tStart = t;  // (not accounting for frame time here)
      feedback_memory.frameNStart = frameN;  // exact frame index
      
      feedback_memory.setAutoDraw(true);
    }
    
    
    // if feedback_memory is active this frame...
    if (feedback_memory.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_memory.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      feedback_memory.tStop = t;  // not accounting for scr refresh
      feedback_memory.frameNStop = frameN;  // exact frame index
      // update status
      feedback_memory.status = PsychoJS.Status.FINISHED;
      feedback_memory.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fb_recogComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fb_recogRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fb_recog' ---
    for (const thisComponent of fb_recogComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fb_recog.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fb_recogMaxDurationReached) {
        fb_recogClock.add(fb_recogMaxDuration);
    } else {
        fb_recogClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pauseMaxDurationReached;
var pauseMaxDuration;
var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pause' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    pauseClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    pauseMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('pause.started', globalClock.getTime());
    pauseMaxDuration = null
    // keep track of which components have finished
    pauseComponents = [];
    pauseComponents.push(pause_text);
    
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pause' ---
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pause_text* updates
    if (t >= 0.0 && pause_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pause_text.tStart = t;  // (not accounting for frame time here)
      pause_text.frameNStart = frameN;  // exact frame index
      
      pause_text.setAutoDraw(true);
    }
    
    
    // if pause_text is active this frame...
    if (pause_text.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (pause_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      pause_text.tStop = t;  // not accounting for scr refresh
      pause_text.frameNStop = frameN;  // exact frame index
      // update status
      pause_text.status = PsychoJS.Status.FINISHED;
      pause_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pause' ---
    for (const thisComponent of pauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('pause.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (pauseMaxDurationReached) {
        pauseClock.add(pauseMaxDuration);
    } else {
        pauseClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr_3MaxDurationReached;
var _key_resp_5_allKeys;
var instr_3MaxDuration;
var instr_3Components;
function instr_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_3Clock.reset();
    routineTimer.reset();
    instr_3MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('instr_3.started', globalClock.getTime());
    instr_3MaxDuration = null
    // keep track of which components have finished
    instr_3Components = [];
    instr_3Components.push(text_4);
    instr_3Components.push(key_resp_5);
    
    for (const thisComponent of instr_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instr_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_3' ---
    // get current time
    t = instr_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // if text_4 is active this frame...
    if (text_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.5 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    // if key_resp_5 is active this frame...
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_3' ---
    for (const thisComponent of instr_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "instr_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var memorMaxDurationReached;
var memorMaxDuration;
var memorComponents;
function memorRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memor' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    memorClock.reset(routineTimer.getTime());
    routineTimer.add(1.100000);
    memorMaxDurationReached = false;
    // update component parameters for each repeat
    square1.setFillColor(new util.Color(color_1));
    square1.setPos([pos_sq_x1_1, pos_sq_y1_1]);
    square1.setLineColor(new util.Color(color_1));
    square2.setFillColor(new util.Color(color_2));
    square2.setPos([pos_sq_x2_1, pos_sq_y2_1]);
    square2.setLineColor(new util.Color(color_2));
    square3.setFillColor(new util.Color(color_3));
    square3.setPos([pos_sq_x3_1, pos_sq_y3_1]);
    square3.setLineColor(new util.Color(color_3));
    square4.setFillColor(new util.Color(color_4));
    square4.setPos([pos_sq_x4_1, pos_sq_y4_1]);
    square4.setLineColor(new util.Color(color_4));
    psychoJS.experiment.addData('memor.started', globalClock.getTime());
    memorMaxDuration = null
    // keep track of which components have finished
    memorComponents = [];
    memorComponents.push(fix1);
    memorComponents.push(square1);
    memorComponents.push(square2);
    memorComponents.push(square3);
    memorComponents.push(square4);
    memorComponents.push(fix2);
    
    for (const thisComponent of memorComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function memorRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memor' ---
    // get current time
    t = memorClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix1* updates
    if (t >= 0.0 && fix1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix1.tStart = t;  // (not accounting for frame time here)
      fix1.frameNStart = frameN;  // exact frame index
      
      fix1.setAutoDraw(true);
    }
    
    
    // if fix1 is active this frame...
    if (fix1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix1.tStop = t;  // not accounting for scr refresh
      fix1.frameNStop = frameN;  // exact frame index
      // update status
      fix1.status = PsychoJS.Status.FINISHED;
      fix1.setAutoDraw(false);
    }
    
    
    // *square1* updates
    if (t >= 0.5 && square1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square1.tStart = t;  // (not accounting for frame time here)
      square1.frameNStart = frameN;  // exact frame index
      
      square1.setAutoDraw(true);
    }
    
    
    // if square1 is active this frame...
    if (square1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square1.tStop = t;  // not accounting for scr refresh
      square1.frameNStop = frameN;  // exact frame index
      // update status
      square1.status = PsychoJS.Status.FINISHED;
      square1.setAutoDraw(false);
    }
    
    
    // *square2* updates
    if (t >= 0.5 && square2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square2.tStart = t;  // (not accounting for frame time here)
      square2.frameNStart = frameN;  // exact frame index
      
      square2.setAutoDraw(true);
    }
    
    
    // if square2 is active this frame...
    if (square2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square2.tStop = t;  // not accounting for scr refresh
      square2.frameNStop = frameN;  // exact frame index
      // update status
      square2.status = PsychoJS.Status.FINISHED;
      square2.setAutoDraw(false);
    }
    
    
    // *square3* updates
    if (t >= 0.5 && square3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square3.tStart = t;  // (not accounting for frame time here)
      square3.frameNStart = frameN;  // exact frame index
      
      square3.setAutoDraw(true);
    }
    
    
    // if square3 is active this frame...
    if (square3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square3.tStop = t;  // not accounting for scr refresh
      square3.frameNStop = frameN;  // exact frame index
      // update status
      square3.status = PsychoJS.Status.FINISHED;
      square3.setAutoDraw(false);
    }
    
    
    // *square4* updates
    if (t >= 0.5 && square4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square4.tStart = t;  // (not accounting for frame time here)
      square4.frameNStart = frameN;  // exact frame index
      
      square4.setAutoDraw(true);
    }
    
    
    // if square4 is active this frame...
    if (square4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square4.tStop = t;  // not accounting for scr refresh
      square4.frameNStop = frameN;  // exact frame index
      // update status
      square4.status = PsychoJS.Status.FINISHED;
      square4.setAutoDraw(false);
    }
    
    
    // *fix2* updates
    if (t >= 0.6 && fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix2.tStart = t;  // (not accounting for frame time here)
      fix2.frameNStart = frameN;  // exact frame index
      
      fix2.setAutoDraw(true);
    }
    
    
    // if fix2 is active this frame...
    if (fix2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.6 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix2.tStop = t;  // not accounting for scr refresh
      fix2.frameNStop = frameN;  // exact frame index
      // update status
      fix2.status = PsychoJS.Status.FINISHED;
      fix2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of memorComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memorRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memor' ---
    for (const thisComponent of memorComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('memor.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (memorMaxDurationReached) {
        memorClock.add(memorMaxDuration);
    } else {
        memorClock.add(1.100000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var recogMaxDurationReached;
var _key_resp_3_allKeys;
var recogMaxDuration;
var recogComponents;
function recogRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'recog' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    recogClock.reset();
    routineTimer.reset();
    recogMaxDurationReached = false;
    // update component parameters for each repeat
    square_1.setFillColor(new util.Color(color_1));
    square_1.setPos([pos_sq_x1_1, pos_sq_y1_1]);
    square_1.setLineColor(new util.Color(color_1));
    square_2.setFillColor(new util.Color(color_2));
    square_2.setPos([pos_sq_x2_1, pos_sq_y2_1]);
    square_2.setLineColor(new util.Color(color_2));
    square_3.setFillColor(new util.Color(color_3));
    square_3.setPos([pos_sq_x3_1, pos_sq_y3_1]);
    square_3.setLineColor(new util.Color(color_3));
    square_4.setFillColor(new util.Color(color_4));
    square_4.setPos([pos_sq_x4_1, pos_sq_y4_1]);
    square_4.setLineColor(new util.Color(color_4));
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('recog.started', globalClock.getTime());
    recogMaxDuration = null
    // keep track of which components have finished
    recogComponents = [];
    recogComponents.push(fix1_1);
    recogComponents.push(square_1);
    recogComponents.push(square_2);
    recogComponents.push(square_3);
    recogComponents.push(square_4);
    recogComponents.push(key_resp_3);
    
    for (const thisComponent of recogComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function recogRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'recog' ---
    // get current time
    t = recogClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix1_1* updates
    if (t >= 0.0 && fix1_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix1_1.tStart = t;  // (not accounting for frame time here)
      fix1_1.frameNStart = frameN;  // exact frame index
      
      fix1_1.setAutoDraw(true);
    }
    
    
    // if fix1_1 is active this frame...
    if (fix1_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fix1_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      fix1_1.tStop = t;  // not accounting for scr refresh
      fix1_1.frameNStop = frameN;  // exact frame index
      // update status
      fix1_1.status = PsychoJS.Status.FINISHED;
      fix1_1.setAutoDraw(false);
    }
    
    
    // *square_1* updates
    if (t >= 0.5 && square_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_1.tStart = t;  // (not accounting for frame time here)
      square_1.frameNStart = frameN;  // exact frame index
      
      square_1.setAutoDraw(true);
    }
    
    
    // if square_1 is active this frame...
    if (square_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square_1.tStop = t;  // not accounting for scr refresh
      square_1.frameNStop = frameN;  // exact frame index
      // update status
      square_1.status = PsychoJS.Status.FINISHED;
      square_1.setAutoDraw(false);
    }
    
    
    // *square_2* updates
    if (t >= 0.5 && square_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_2.tStart = t;  // (not accounting for frame time here)
      square_2.frameNStart = frameN;  // exact frame index
      
      square_2.setAutoDraw(true);
    }
    
    
    // if square_2 is active this frame...
    if (square_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square_2.tStop = t;  // not accounting for scr refresh
      square_2.frameNStop = frameN;  // exact frame index
      // update status
      square_2.status = PsychoJS.Status.FINISHED;
      square_2.setAutoDraw(false);
    }
    
    
    // *square_3* updates
    if (t >= 0.5 && square_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_3.tStart = t;  // (not accounting for frame time here)
      square_3.frameNStart = frameN;  // exact frame index
      
      square_3.setAutoDraw(true);
    }
    
    
    // if square_3 is active this frame...
    if (square_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square_3.tStop = t;  // not accounting for scr refresh
      square_3.frameNStop = frameN;  // exact frame index
      // update status
      square_3.status = PsychoJS.Status.FINISHED;
      square_3.setAutoDraw(false);
    }
    
    
    // *square_4* updates
    if (t >= 0.5 && square_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      square_4.tStart = t;  // (not accounting for frame time here)
      square_4.frameNStart = frameN;  // exact frame index
      
      square_4.setAutoDraw(true);
    }
    
    
    // if square_4 is active this frame...
    if (square_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.5 + 5.8 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (square_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      square_4.tStop = t;  // not accounting for scr refresh
      square_4.frameNStop = frameN;  // exact frame index
      // update status
      square_4.status = PsychoJS.Status.FINISHED;
      square_4.setAutoDraw(false);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.5 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    // if key_resp_3 is active this frame...
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['s','d'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_3.keys == cor_ans) {
            key_resp_3.corr = 1;
        } else {
            key_resp_3.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recogComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recogRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'recog' ---
    for (const thisComponent of recogComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('recog.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_3.keys === undefined) {
      if (['None','none',undefined].includes(cor_ans)) {
         key_resp_3.corr = 1;  // correct non-response
      } else {
         key_resp_3.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    psychoJS.experiment.addData('key_resp_3.corr', key_resp_3.corr);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "recog" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr_4MaxDurationReached;
var _key_resp_4_allKeys;
var instr_4MaxDuration;
var instr_4Components;
function instr_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr_4' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instr_4Clock.reset();
    routineTimer.reset();
    instr_4MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('instr_4.started', globalClock.getTime());
    instr_4MaxDuration = null
    // keep track of which components have finished
    instr_4Components = [];
    instr_4Components.push(text_5);
    instr_4Components.push(key_resp_4);
    
    for (const thisComponent of instr_4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instr_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr_4' ---
    // get current time
    t = instr_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // if text_5 is active this frame...
    if (text_5.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.5 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    // if key_resp_4 is active this frame...
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: 'space', waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instr_4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr_4' ---
    for (const thisComponent of instr_4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instr_4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "instr_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fix_3MaxDurationReached;
var fix_3MaxDuration;
var fix_3Components;
function fix_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fix_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    fix_3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    fix_3MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fix_3.started', globalClock.getTime());
    fix_3MaxDuration = null
    // keep track of which components have finished
    fix_3Components = [];
    fix_3Components.push(text_6);
    
    for (const thisComponent of fix_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fix_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fix_3' ---
    // get current time
    t = fix_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    
    // if text_6 is active this frame...
    if (text_6.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_6.tStop = t;  // not accounting for scr refresh
      text_6.frameNStop = frameN;  // exact frame index
      // update status
      text_6.status = PsychoJS.Status.FINISHED;
      text_6.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fix_3' ---
    for (const thisComponent of fix_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fix_3.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (fix_3MaxDurationReached) {
        fix_3Clock.add(fix_3MaxDuration);
    } else {
        fix_3Clock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var final_recogMaxDurationReached;
var _recog_ans_allKeys;
var final_recogMaxDuration;
var final_recogComponents;
function final_recogRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'final_recog' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    final_recogClock.reset();
    routineTimer.reset();
    final_recogMaxDurationReached = false;
    // update component parameters for each repeat
    recog_ans.keys = undefined;
    recog_ans.rt = undefined;
    _recog_ans_allKeys = [];
    image1.setPos([posx1, posy1]);
    image1.setImage(letter1);
    image2.setPos([posx2, posy2]);
    image2.setImage(letter2);
    image3.setPos([posx3, posy3]);
    image3.setImage(letter3);
    image4.setPos([posx4, posy4]);
    image4.setImage(letter4);
    image5.setPos([posx5, posy5]);
    image5.setImage(letter5);
    image6.setPos([posx6, posy6]);
    image6.setImage(letter6);
    image7.setPos([posx7, posy7]);
    image7.setImage(letter7);
    image8.setPos([posx8, posy8]);
    image8.setImage(letter8);
    image9.setPos([posx9, posy9]);
    image9.setImage(letter9);
    image10.setPos([posx10, posy10]);
    image10.setImage(letter10);
    image11.setPos([posx11, posy11]);
    image11.setImage(letter11);
    image12.setPos([posx12, posy12]);
    image12.setImage(letter12);
    psychoJS.experiment.addData('final_recog.started', globalClock.getTime());
    final_recogMaxDuration = null
    // keep track of which components have finished
    final_recogComponents = [];
    final_recogComponents.push(recog_ans);
    final_recogComponents.push(image1);
    final_recogComponents.push(image2);
    final_recogComponents.push(image3);
    final_recogComponents.push(image4);
    final_recogComponents.push(image5);
    final_recogComponents.push(image6);
    final_recogComponents.push(image7);
    final_recogComponents.push(image8);
    final_recogComponents.push(image9);
    final_recogComponents.push(image10);
    final_recogComponents.push(image11);
    final_recogComponents.push(image12);
    
    for (const thisComponent of final_recogComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function final_recogRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'final_recog' ---
    // get current time
    t = final_recogClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recog_ans* updates
    if (t >= 0.0 && recog_ans.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recog_ans.tStart = t;  // (not accounting for frame time here)
      recog_ans.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { recog_ans.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { recog_ans.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { recog_ans.clearEvents(); });
    }
    
    // if recog_ans is active this frame...
    if (recog_ans.status === PsychoJS.Status.STARTED) {
      let theseKeys = recog_ans.getKeys({keyList: ['left','right'], waitRelease: false});
      _recog_ans_allKeys = _recog_ans_allKeys.concat(theseKeys);
      if (_recog_ans_allKeys.length > 0) {
        recog_ans.keys = _recog_ans_allKeys[_recog_ans_allKeys.length - 1].name;  // just the last key pressed
        recog_ans.rt = _recog_ans_allKeys[_recog_ans_allKeys.length - 1].rt;
        recog_ans.duration = _recog_ans_allKeys[_recog_ans_allKeys.length - 1].duration;
        // was this correct?
        if (recog_ans.keys == direction) {
            recog_ans.corr = 1;
        } else {
            recog_ans.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *image1* updates
    if (t >= 0.0 && image1.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image1.setOri(orient1, false);
      // keep track of start time/frame for later
      image1.tStart = t;  // (not accounting for frame time here)
      image1.frameNStart = frameN;  // exact frame index
      
      image1.setAutoDraw(true);
    }
    
    
    // if image1 is active this frame...
    if (image1.status === PsychoJS.Status.STARTED) {
      // update params
      image1.setOri(orient1, false);
    }
    
    
    // *image2* updates
    if (t >= 0.0 && image2.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image2.setOri(orient2, false);
      // keep track of start time/frame for later
      image2.tStart = t;  // (not accounting for frame time here)
      image2.frameNStart = frameN;  // exact frame index
      
      image2.setAutoDraw(true);
    }
    
    
    // if image2 is active this frame...
    if (image2.status === PsychoJS.Status.STARTED) {
      // update params
      image2.setOri(orient2, false);
    }
    
    
    // *image3* updates
    if (t >= 0.0 && image3.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image3.setOri(orient3, false);
      // keep track of start time/frame for later
      image3.tStart = t;  // (not accounting for frame time here)
      image3.frameNStart = frameN;  // exact frame index
      
      image3.setAutoDraw(true);
    }
    
    
    // if image3 is active this frame...
    if (image3.status === PsychoJS.Status.STARTED) {
      // update params
      image3.setOri(orient3, false);
    }
    
    
    // *image4* updates
    if (t >= 0.0 && image4.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image4.setOri(orient4, false);
      // keep track of start time/frame for later
      image4.tStart = t;  // (not accounting for frame time here)
      image4.frameNStart = frameN;  // exact frame index
      
      image4.setAutoDraw(true);
    }
    
    
    // if image4 is active this frame...
    if (image4.status === PsychoJS.Status.STARTED) {
      // update params
      image4.setOri(orient4, false);
    }
    
    
    // *image5* updates
    if (t >= 0.0 && image5.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image5.setOri(orient5, false);
      // keep track of start time/frame for later
      image5.tStart = t;  // (not accounting for frame time here)
      image5.frameNStart = frameN;  // exact frame index
      
      image5.setAutoDraw(true);
    }
    
    
    // if image5 is active this frame...
    if (image5.status === PsychoJS.Status.STARTED) {
      // update params
      image5.setOri(orient5, false);
    }
    
    
    // *image6* updates
    if (t >= 0.0 && image6.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image6.setOri(orient6, false);
      // keep track of start time/frame for later
      image6.tStart = t;  // (not accounting for frame time here)
      image6.frameNStart = frameN;  // exact frame index
      
      image6.setAutoDraw(true);
    }
    
    
    // if image6 is active this frame...
    if (image6.status === PsychoJS.Status.STARTED) {
      // update params
      image6.setOri(orient6, false);
    }
    
    
    // *image7* updates
    if (t >= 0.0 && image7.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image7.setOri(orient7, false);
      // keep track of start time/frame for later
      image7.tStart = t;  // (not accounting for frame time here)
      image7.frameNStart = frameN;  // exact frame index
      
      image7.setAutoDraw(true);
    }
    
    
    // if image7 is active this frame...
    if (image7.status === PsychoJS.Status.STARTED) {
      // update params
      image7.setOri(orient7, false);
    }
    
    
    // *image8* updates
    if (t >= 0.0 && image8.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image8.setOri(orient8, false);
      // keep track of start time/frame for later
      image8.tStart = t;  // (not accounting for frame time here)
      image8.frameNStart = frameN;  // exact frame index
      
      image8.setAutoDraw(true);
    }
    
    
    // if image8 is active this frame...
    if (image8.status === PsychoJS.Status.STARTED) {
      // update params
      image8.setOri(orient8, false);
    }
    
    
    // *image9* updates
    if (t >= 0.0 && image9.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image9.setOri(orient9, false);
      // keep track of start time/frame for later
      image9.tStart = t;  // (not accounting for frame time here)
      image9.frameNStart = frameN;  // exact frame index
      
      image9.setAutoDraw(true);
    }
    
    
    // if image9 is active this frame...
    if (image9.status === PsychoJS.Status.STARTED) {
      // update params
      image9.setOri(orient9, false);
    }
    
    
    // *image10* updates
    if (t >= 0.0 && image10.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image10.setOri(orient10, false);
      // keep track of start time/frame for later
      image10.tStart = t;  // (not accounting for frame time here)
      image10.frameNStart = frameN;  // exact frame index
      
      image10.setAutoDraw(true);
    }
    
    
    // if image10 is active this frame...
    if (image10.status === PsychoJS.Status.STARTED) {
      // update params
      image10.setOri(orient10, false);
    }
    
    
    // *image11* updates
    if (t >= 0.0 && image11.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image11.setOri(orient11, false);
      // keep track of start time/frame for later
      image11.tStart = t;  // (not accounting for frame time here)
      image11.frameNStart = frameN;  // exact frame index
      
      image11.setAutoDraw(true);
    }
    
    
    // if image11 is active this frame...
    if (image11.status === PsychoJS.Status.STARTED) {
      // update params
      image11.setOri(orient11, false);
    }
    
    
    // *image12* updates
    if (t >= 0.0 && image12.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      image12.setOri(orient12, false);
      // keep track of start time/frame for later
      image12.tStart = t;  // (not accounting for frame time here)
      image12.frameNStart = frameN;  // exact frame index
      
      image12.setAutoDraw(true);
    }
    
    
    // if image12 is active this frame...
    if (image12.status === PsychoJS.Status.STARTED) {
      // update params
      image12.setOri(orient12, false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of final_recogComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function final_recogRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'final_recog' ---
    for (const thisComponent of final_recogComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('final_recog.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (recog_ans.keys === undefined) {
      if (['None','none',undefined].includes(direction)) {
         recog_ans.corr = 1;  // correct non-response
      } else {
         recog_ans.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(recog_ans.corr, level);
    }
    psychoJS.experiment.addData('recog_ans.keys', recog_ans.keys);
    psychoJS.experiment.addData('recog_ans.corr', recog_ans.corr);
    if (typeof recog_ans.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('recog_ans.rt', recog_ans.rt);
        psychoJS.experiment.addData('recog_ans.duration', recog_ans.duration);
        routineTimer.reset();
        }
    
    recog_ans.stop();
    // the Routine "final_recog" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endMaxDurationReached;
var endMaxDuration;
var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    endClock.reset(routineTimer.getTime());
    routineTimer.add(1.500000);
    endMaxDurationReached = false;
    // update component parameters for each repeat
    // Отключаем скачивание через браузер
    psychoJS._saveResults = 0;
    
    // Именуем файлы
    let filename = psychoJS.experiment._participant +  '_' + psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
    // Достаем дата обджект из эксперимента
    let dataObj = psychoJS._experiment._trialsData;
    // Конвертируем в csv
    let data = [Object.keys(dataObj[0])].concat(dataObj).map(it => {
        return Object.values(it).toString()
    }).join('\n')
    // Отправляем на OSF через DataPipe
    console.log('Saving data...');
    fetch('https://pipe.jspsych.org/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Accept: '*/*',
         },   
         body: JSON.stringify({
            experimentID: 'H51PXszKneD1', // * DATAPIPE EXP ID*
            filename: filename, 
            data: data,
         }),
    }).then(response => response.json()).then(data => {
    // Кидаем в консоль результат и выходим из эксперимента
        console.log(data);
        quitPsychoJS();
    })
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    endMaxDuration = null
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_2);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_2.tStop = t;  // not accounting for scr refresh
      text_2.frameNStop = frameN;  // exact frame index
      // update status
      text_2.status = PsychoJS.Status.FINISHED;
      text_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (endMaxDurationReached) {
        endClock.add(endMaxDuration);
    } else {
        endClock.add(1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
