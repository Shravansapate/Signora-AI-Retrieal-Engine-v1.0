'use client';

import { useEffect, useRef, useState } from 'react';
import AvatarViewer from './AvatarViewer.jsx';
import { LiveDisplay } from '../services/live-display.mjs';

export default function DisplayConsole() {
  const [token, setToken] = useState('');
  const [device, setDevice] = useState('');
  const [connected, setConnected] = useState(false);
  const [status, setStatus] = useState({ state: 'DISCONNECTED' });
  const [playback, setPlayback] = useState({ state: 'IDLE' });
  const viewer = useRef(null), session = useRef(null);
  useEffect(() => () => session.current?.close(), []);
  const connect = event => {
    event.preventDefault();
    try {
      session.current = new LiveDisplay({ displayId: device, token, player: viewer.current,
        onStatus: update => setStatus(previous => ({ ...previous, ...update })) });
      session.current.connect(); setConnected(true);
    } catch (error) { setStatus({ state: 'ERROR', detail: error.message }); }
  };
  return <main className="workspace live-display">
    <h1>Live railway announcements</h1>
    <p role="status">Connection: {status.state} · Signing: {playback.state}</p>
    {!connected ? <form onSubmit={connect}>
      <label>Display ID<input value={device} onChange={event => setDevice(event.target.value)} required /></label>
      <label>Display access token<input type="password" value={token} onChange={event => setToken(event.target.value)} autoComplete="off" required /></label>
      <button type="submit">Connect display</button>
    </form> : <button onClick={() => { session.current?.close(); session.current = null; setConnected(false); setToken(''); setStatus({ state: 'DISCONNECTED' }); }}>Disconnect display</button>}
    <p className="caption-area" aria-live="assertive">{status.caption || 'No current announcement.'}</p>
    {status.state === 'CONNECTED' && !status.caption && <p>Waiting for this station's next announcement. Enter text or record voice on the <a href="/announcements" target="_blank" rel="noreferrer">Announcements page</a> and select Play announcement.</p>}
    {status.detail && <p role="alert">{status.detail}</p>}
    {playback.error?.message && <p role="alert">{playback.error.message}</p>}
    <AvatarViewer ref={viewer} token={token} onState={snapshot => { setPlayback(snapshot); session.current?.onPlayback(snapshot); }} />
  </main>;
}
