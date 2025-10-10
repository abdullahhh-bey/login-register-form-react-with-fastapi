from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

#configurations
connect = ConnectionConfig(
    MAIL_USERNAME="abdullahamirr9@gmail.com",
    MAIL_PASSWORD="ggbowcuqlyrxyrtc", 
    MAIL_FROM="abdullahamirr9@gmail.com", 
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)

#email sending service
async def email_sending_service(token : str , to_email : str):
    verify_token = token
    sub = "Verify your account"
    message = f"""
        <h2>Welcome!</h2>
        <p>Copy the link below to verify your email:</p>
        <a>{verify_token}</a>
        <p>This link will expire in 30 minutes.</p>
        """
    
    m = MessageSchema(
        recipients= [to_email],
        subject=sub,
        body=message,
        subtype="html"
    )
    
    service = FastMail(connect)
    await service.send_message(m)
    