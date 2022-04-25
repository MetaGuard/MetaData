using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ReactionTime : MonoBehaviour {
    public MeshCollider btn;
    bool leftIn = false;
    bool rightIn = false;
    public AudioSource src;
    public AudioClip click;
    public AudioClip win;
    public GameObject movingButton;
    public GameObject r1;
    public GameObject r2;
    public GameObject r3;
    public GameObject r4;
    public GameObject r5;
    public GameObject g1;
    public GameObject g2;
    public GameObject g3;
    public GameObject g4;
    public GameObject g5;
    int active = 1;
    bool go = true;

    void Start() {
      StartCoroutine(ExampleCoroutine());
      g1.SetActive(false);
      g2.SetActive(false);
      g3.SetActive(false);
      g4.SetActive(false);
      g5.SetActive(false);
    }

    IEnumerator ExampleCoroutine() {
      bool exit = true;
      while(exit) {
        if (active == 1) {
          go = false;
          int randomValue1 = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue1);
          g1.SetActive(true);
          go = true;
          yield return new WaitForSeconds(1.0f);
          g1.SetActive(false);
          go = false;
          int randomValue = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue);
        } else if (active == 2) {
          go = false;
          int randomValue1 = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue1);
          g1.SetActive(false);
          r1.SetActive(false);
          g2.SetActive(true);
          go = true;
          yield return new WaitForSeconds(0.75f);
          g2.SetActive(false);
          go = false;
          int randomValue = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue);
        } else if (active == 3) {
          go = false;
          int randomValue1 = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue1);
          g2.SetActive(false);
          r2.SetActive(false);
          g3.SetActive(true);
          go = true;
          yield return new WaitForSeconds(0.5f);
          g3.SetActive(false);
          go = false;
          int randomValue = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue);
        } else if (active == 4) {
          go = false;
          int randomValue1 = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue1);
          g3.SetActive(false);
          r3.SetActive(false);
          g4.SetActive(true);
          go = true;
          yield return new WaitForSeconds(0.25f);
          g4.SetActive(false);
          go = false;
          int randomValue = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue);
        } else if (active == 5) {
          go = false;
          int randomValue1 = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue1);
          g4.SetActive(false);
          r4.SetActive(false);
          g5.SetActive(true);
          go = true;
          yield return new WaitForSeconds(0.15f);
          g5.SetActive(false);
          go = false;
          int randomValue = Random.Range(1, 4);
          yield return new WaitForSeconds(randomValue);
        } else if (active >= 6) {
          go = false;
          g5.SetActive(false);
          r5.SetActive(false);
          exit = false;
        }
      }
    }


    void OnTriggerEnter(Collider other) {
      if (!(leftIn || rightIn)) {
        src.PlayOneShot(click, 1f);
        if (go) {
          go = false;
          src.PlayOneShot(win, 1f);
          this.active++;
          if (active == 2) {
            g1.SetActive(false);
            r1.SetActive(false);
          } else if (active == 3) {
            g2.SetActive(false);
            r2.SetActive(false);
          } else if (active == 4) {
            g3.SetActive(false);
            r3.SetActive(false);
          } else if (active == 5) {
            g4.SetActive(false);
            r4.SetActive(false);
          } else if (active >= 6) {
            g5.SetActive(false);
            r5.SetActive(false);
          }
        }
      }
      if(other.gameObject.name == "LeftController") {
        leftIn = true;
      } else if (other.gameObject.name == "RightController") {
        rightIn = true;
      }
    }

    void OnTriggerExit(Collider other) {
      if(other.gameObject.name == "LeftController") {
        leftIn = false;
      } else if (other.gameObject.name == "RightController") {
        rightIn = false;
      }
    }

    void Update() {
      if (leftIn || rightIn) {
        movingButton.transform.position = new Vector3(20.159f, 0.805f, -16.117f);
      } else {
        movingButton.transform.position = new Vector3(20.159f, 0.865f, -16.117f);
      }
    }
}
