import React, {useState, useEffect} from 'react';
import styled from "styled-components";
import "./icon.css";
import { BsPerson } from "react-icons/bs";
import { AiOutlineLock } from "react-icons/ai";
import Axios from 'axios';

const LoginContainer = styled.div`
    width: 700px;
    height: 480px;
    border: 3px solid rgba(123, 207, 255, 1);
    border-radius: 20px;
    margin: 100px auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #fff;
`;

export const LoginId = styled.div`
    width: 500px;
    height: 50px;
    border: 3px solid rgba(123, 207, 255, 1);
    border-radius: 15px 15px 0 0;
    display: flex;
    align-items: center;
`;

export const LoginPw = styled(LoginId)`
    border-radius: 0 0 15px 15px;
    border-top: none;
`;

export const LoginText = styled.input`
    width: 85%;
    height: 100%;
    padding-top: 0;
    padding-bottom: 0;
    margin-left: 3%;
    margin-right: 5%;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 18px;
    border: none;
    outline: none;
`;

const LoginMid = styled.div`
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 18px;
    color: #9e9e9e;
    width: 505px;
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
`;

const Remember = styled.input`
    width: 25px;
    height: 25px;
    border: 2px solid #9e9e9e;
    margin-right: 5px;
`;

const FindIdPw = styled.div`
    font-size: 16px;
    margin-top: 5px;
`;

const LoginBtn = styled.button`
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 30px;
    color: #fff;
    width: 506px;
    height: 60px;
    border-radius: 15px;
    border: none;
    margin-top: 10px;
    background: rgba(36, 176, 255, 1);
`;

const LoginBot = styled(LoginMid)`
    font-size: 16px;
`;

const RegisterBtn = styled.button`
    height: 30px;
    margin-top: 8.2px;
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 16px;
    color: rgba(36, 176, 255, 1);
    border: 2px solid rgba(36, 176, 255, 1);
    border-radius: 10px;
    background-color: transparent;
`;

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const inputEmail = (e) => {
        setEmail(e.target.value);
    }

    const inputPassword = (e) => {
        setPassword(e.target.value);
    }

    const onClickLogin = () => {
        Axios.post('', {
            userEmail : email,
            userPassword: password
        })
        .then(res => {
            console.log(res);
            console.log(res.data.email);
            console.log(res.data.password);
            if(res.data.email !== email) {
                alert('잘못된 이메일입니다');
            } else if(res.data.password === password) {
                alert('잘못된 비밀번호입니다');
            } else if(res.data.email === email) {
                sessionStorage.setItem('userEmail', email);
                window.location.replace('/');
            }
        })
        .catch()
    }

    useEffect(() => {
        Axios.get('')
        .then(res => console.log(res))
        .catch()
    },[])

    return(
        <div style={{background: '#f9f9f9', height: '100%', display: 'flex'}}>
            <LoginContainer>
                <h1 style={{fontFamily: "'Noto Sans KR', sans-serif", fontSize: 30, marginTop: 50, marginBottom: 45}}>로그인</h1>
                <form >
                    <LoginId>
                        <BsPerson size='25' className='loginIdPerson'/>
                        <LoginText type = "email" placeholder="아이디" value={email} onChange={inputEmail} />
                    </LoginId>
                    <LoginPw>
                        <AiOutlineLock size='25' className='loginPwLock' />
                        <LoginText type = "password" placeholder="비밀번호" value={password} onChange={inputPassword} />
                    </LoginPw>
                </form>
                <LoginMid>
                    <label style={{display: 'flex', alignItems: 'center'}}><Remember type="checkbox" />자동 로그인</label>
                    <FindIdPw>아이디 찾기 / 비밀번호 찾기</FindIdPw>
                </LoginMid>
                <LoginBtn type='button' onClick={onClickLogin} >로그인</LoginBtn>
                <LoginBot>
                    아끼자의 회원이 아니신가요?<br></br>지금 당장 가입해서 아껴보세요
                    <RegisterBtn>회원가입</RegisterBtn>
                </LoginBot>
            </LoginContainer>
        </div>
    );
}

export default Login;
