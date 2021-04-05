const videos = ['Netflix', 'Youtube', 'Vimeo', 'Vine'];

const tabsBeforeIndex = videos.slice(0, 2);
const tabsAfterIndex = videos.slice(3);
const finalVideo = tabsBeforeIndex.concat(tabsAfterIndex);
console.log(finalVideo);

const work = ['Gmail', 'Inbox', 'Work mail', 'Docs', 'freeCodeCamp'];
const workTabsBeforeIndex = work.slice(0, 1);
const workTabsAfterIndex = work.slice(2);
const finalWork = workTabsBeforeIndex.concat(workTabsAfterIndex);
console.log(finalWork);