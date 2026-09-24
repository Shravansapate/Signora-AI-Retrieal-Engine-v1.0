'use client';

import { useState } from 'react';
import LibraryManager from './LibraryManager.jsx';
import TemplateManager from './TemplateManager.jsx';
import { AuditManager, DisplayManager, ImportManager, StationManager } from './OperationsManager.jsx';
import { Feedback, Field, Navigation, useWorkspace } from './workspace.jsx';

const TABS = [['library','Library',LibraryManager],['templates','Templates & coverage',TemplateManager],
  ['imports','Imports',ImportManager],['stations','Stations',StationManager],['displays','Displays',DisplayManager],['audit','Audit',AuditManager]];

export default function AdminConsole() {
  const [credential, setCredential] = useState(''), [token, setToken] = useState(''), [identity, setIdentity] = useState(null), [tab, setTab] = useState('library');
  const work = useWorkspace(credential.trim()), admin = identity?.roles.includes('admin');
  const visible = TABS.filter(([key]) => admin || ['library','templates'].includes(key));
  const Component = visible.find(([key]) => key === tab)?.[2] ?? LibraryManager;
  return <><a className="skip-link" href="#management">Skip to management workspace</a><Navigation /><main id="management">
    <div className="page-heading"><div><p className="eyebrow">DEVELOPER & CONTENT MANAGEMENT</p><h1>Station, library and operations</h1><p>Administrators configure stations, ingest datasets and manage motion versions. Reviewers inspect content and construction coverage.</p></div></div>
    {!identity ? <section className="panel management-section"><form onSubmit={e => { e.preventDefault(); work.run('Checking workspace access', async api => {
      const result = await api('/api/v1/session');
      if (!result.roles.some(role => ['admin','reviewer'].includes(role))) throw new Error('A content reviewer or administrator credential is required.');
      setIdentity(result); setToken(credential.trim()); setCredential('');
      const requested = new URLSearchParams(window.location.search).get('tab');
      setTab(TABS.some(([key]) => key === requested) && (result.roles.includes('admin') || ['library','templates'].includes(requested)) ? requested : result.roles.includes('admin') ? 'stations' : 'library');
    }); }}><Field label="Management access token" value={credential} onChange={setCredential} type="password" autoComplete="off" disabled={!!work.busy} />
      <button className="primary" disabled={!!work.busy || !credential.trim()}>Connect management</button></form><Feedback {...work} /></section>
      : <><section className="panel connected-row"><span>{identity.subject} · {identity.roles.join(', ')} · credentials held in memory</span><button onClick={() => { setIdentity(null); setToken(''); setCredential(''); }}>Disconnect management</button></section>
        <nav className="workspace-tabs" aria-label="Management sections">{visible.map(([key,label]) => <button key={key} aria-current={key === tab ? 'page' : undefined} onClick={() => setTab(key)}>{label}</button>)}</nav>
        <Component key={tab} token={token} admin={admin} />
      </>}
  </main></>;
}
