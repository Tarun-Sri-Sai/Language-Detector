import { Component } from '@angular/core'
import { AppService } from '../app.service'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent {
  textInput: string = ''
  private timeout: boolean = false
  minCharacters: number = 20
  private timeoutMillis: number = 500

  constructor(private http: HttpClient, private app: AppService) { }

  detectLanguage(): void {
    if (this.timeout) {
      return
    }

    this.timeout = true

    if (!this.isValidLength()) {
      this.resetTimeout()
      return
    }

    this.http.post<any>('http://localhost:5000/detect-language', { 'text_input': this.textInput })
      .subscribe({
        next: (response) => { },
        error: (error) => {
          console.error("Couldn't post text due to: ", error)
        }
      })

    this.http.get<any>('http://localhost:5000/detect-language')
      .subscribe({
        next: (response) => {
          this.app.result = response['language_code']
        },
        error: (error) => {
          console.error("Couldn't get language due to: ", error)
        }
      })

    this.http.delete<any>('http://localhost:5000/detect-language')
      .subscribe({
        next: (response) => { },
        error: (error) => {
          console.error("Couldn't delete language data due to: ", error)
        }
      })

    this.resetTimeout()
  }

  isValidLength(): boolean {
    return this.textInput.trim().replaceAll(/\s+/g, ' ').length >= this.minCharacters
  }

  resetTimeout(): void {
    setTimeout(() => {
      this.timeout = false
    }, this.timeoutMillis)
  }
}
